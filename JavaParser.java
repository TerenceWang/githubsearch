import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.sun.source.tree.*;
import com.sun.source.util.JavacTask;
import com.sun.source.util.TreeScanner;
import com.sun.tools.javac.api.JavacTool;
import com.sun.tools.javac.file.JavacFileManager;
import com.sun.tools.javac.util.Context;

import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.ArrayList;

/**
 * Created by terence on 4/23/17.
 */
public class JavaParser {

    private static String filepath;

    private JavacFileManager fileManager;
    private JavacTool javacTool;
//    private JsonObject funcJsonObject;
    private static JsonArray methodsJsonArray = new JsonArray();
    private static JsonArray classJsonArray = new JsonArray();

    public JavaParser() {
        Context context = new Context();
        fileManager = new JavacFileManager(context, true, Charset.defaultCharset());
        javacTool = new JavacTool();
    }

    public JsonObject parseJavaFiles(String filename) {
        filepath = filename;
        methodsJsonArray = new JsonArray();
        classJsonArray = new JsonArray();
        Iterable<? extends JavaFileObject> files = fileManager.getJavaFileObjects(filename);
        JavaCompiler.CompilationTask compilationTask = javacTool.getTask(null, fileManager, null, null, null, files);
        JavacTask javacTask = (JavacTask) compilationTask;
        try {
            Iterable<? extends CompilationUnitTree> result = javacTask.parse();
            for (CompilationUnitTree tree : result) {
                tree.accept(new SourceVisitor(), null);

            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        JsonObject funcJsonObject = new JsonObject();
        funcJsonObject.addProperty("PATH",filename);
        funcJsonObject.add("defined_class",classJsonArray);
        funcJsonObject.add("defined_fun",methodsJsonArray);

//        System.out.println(funcJsonObject.toString());
        return funcJsonObject;
    }

    static class SourceVisitor extends TreeScanner<Void, Void> {

        private String currentPackageName = null;
        @Override
        public Void visitClass(ClassTree node, Void aVoid){
//            formatPtrln("Class name: %s, kind: %s",
//                    node.getSimpleName(), node.getKind());
//            visitModifiers(node.getModifiers(),aVoid);
            JsonObject classJson = new JsonObject();

            if (node.getSimpleName().toString().equals(""))
                return super.visitClass(node, aVoid);

            //Name
            classJson.addProperty("class_name",node.getSimpleName().toString());

            //Modifier
            ModifiersTree modifiersTree = node.getModifiers();
            JsonArray modifier = new JsonArray();
            if(modifiersTree.getFlags().size()!=0){
                for (int i = 0; i < modifiersTree.getFlags().size(); i++) {
                    modifier.add(modifiersTree.getFlags().toArray()[i].toString());
                }
            }
            classJson.add("class_modifier",modifier);

            //Extend
            String extend="";
            if (node.getExtendsClause()!=null){
                extend = node.getExtendsClause().getKind().toString();
            }
            classJson.addProperty("class_extend",extend);

            //implement

            JsonArray implement = new JsonArray();
            if(node.getImplementsClause().size()!=0){
                for (int i = 0; i < node.getImplementsClause().size(); i++) {
                    implement.add(node.getImplementsClause().toArray()[i].toString());
                }
            }
            classJson.add("class_implement",implement);
            classJsonArray.add(classJson);

            return super.visitClass(node, aVoid);
        }
        @Override
        public Void visitModifiers(ModifiersTree node, Void aVoid){
//            if(node.getFlags().size()!=0)
//                System.out.println(node.getFlags().toArray()[0].toString());
//            System.out.println(node.getFlags().size());
            return super.visitModifiers(node,aVoid);
        }
        @Override
        public Void visitMethod(MethodTree node, Void aVoid){
            JsonObject methodJson = new JsonObject();

            //name

            methodJson.addProperty("fun_name",node.getName().toString());

            //method
            ModifiersTree modifiersTree = node.getModifiers();
            JsonArray modifier = new JsonArray();
            if(modifiersTree.getFlags().size()!=0){
                for (int i = 0; i < modifiersTree.getFlags().size(); i++) {
                    modifier.add(modifiersTree.getFlags().toArray()[i].toString());
                }
            }
            methodJson.add("fun_modifier",modifier);

            // input
            JsonArray inputArray = new JsonArray();
            if(node.getParameters().size()!=0){
                for (int i = 0; i < node.getParameters().size(); i++) {
                    JsonObject input = new JsonObject();
                    input.addProperty("input_name",node.getParameters().get(i).getName().toString());
                    input.addProperty("input_type",node.getParameters().get(i).getType().toString());
                    inputArray.add(input);
                }
            }
            methodJson.add("fun_input",inputArray);

            JsonObject returnType = new JsonObject();
            String type = "";
            if(node.getReturnType()!=null){
                type = node.getReturnType().toString();
            }
            methodJson.addProperty("fun_return",type);

            methodsJsonArray.add(methodJson);

//            formatPtrln("Method name: %s, kind: %s， return type: %s",
//                    node.getName(),node.getKind(),node.getReturnType());
//            if (node.getParameters().size()!=0){
//                VariableTree nodee = node.getParameters().get(0);
//                formatPtrln("variable Modifier: %s, name: %s, type: %s, kind: %s, package: %s",
//                        nodee.getNameExpression(), nodee.getName(), nodee.getType(), node.getKind(), currentPackageName);
//            }
//            System.out.println(methodsJsonArray.toString());
            return super.visitMethod(node, aVoid);

        }
        @Override
        public Void visitCompilationUnit(CompilationUnitTree node, Void aVoid) {

//            return null;
            return super.visitCompilationUnit(node, aVoid);
        }

        @Override
        public Void visitVariable(VariableTree node, Void aVoid) {
//            formatPtrln("variable Modifier: %s, name: %s, type: %s, kind: %s, package: %s",
//                    node.getNameExpression(), node.getName(), node.getType(), node.getKind(), currentPackageName);
            return super.visitVariable(node,aVoid);
        }
    }

    public static void formatPtrln(String format, Object... args) {
        System.out.println(String.format(format, args));
    }

    public static ArrayList<JsonObject> jsonlist;
    private static void parserepo(File repo){
        File flist[] = repo.listFiles();
        if (flist == null || flist.length == 0) {
            return ;
        }
        for (File f : flist) {
            if (f.isDirectory()) {
                parserepo(f);
            } else {
                JavaParser parser = new JavaParser();
                if(!f.toString().endsWith(".java")) {
                    continue;
                }
                JsonObject filejson = parser.parseJavaFiles(f.getAbsolutePath());
                jsonlist.add(filejson);
//                System.out.println("file==>" + f.getAbsolutePath());
            }
        }
    }
    public static void writeFile(int count,String repo,JsonArray repoArray){
        filepath = "/Volumes/Transcend/workspace/se_pro/crawler/data/java/jsondata/";
        File ff = new File(filepath+"/file"+Integer.toString(count)+".json");
        if(!ff.exists()){
            try {
                ff.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        try {
            FileWriter writer=new FileWriter(filepath+"/file"+Integer.toString(count)+".json");
            writer.write(repoArray.toString());
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
//        String filename = "./data/Accumulator.java";
//        new JavaParser().parseJavaFiles(filename);
        File file = new File("/Volumes/Transcend/workspace/se_pro/crawler/data/java/data");
        File flist[] = file.listFiles();
        if (flist == null || flist.length == 0) {
            return ;
        }
        int count = 0;
        for (File username : flist) {
            if (username.isDirectory()) {
                File reposlist[] = username.listFiles();
                for (File repo : reposlist){
                    if (!repo.isDirectory())
                        continue;
                    JsonArray repoArray = new JsonArray();
                    jsonlist = new ArrayList<>();
                    parserepo(repo);
                    for (int i = 0; i < jsonlist.size(); i++) {
                        repoArray.add(jsonlist.get(i));
                    }
                    writeFile(count, repo.getName(), repoArray);
                    System.out.println("Processing "+repo.getName()+"...");
                    count++;
                }
            }
        }
    }
}
