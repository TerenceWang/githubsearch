var express = require('express'),
    // ElasticSearchClient = require('elasticsearch'),
    url = require('url');

var app = module.exports = express.createServer();

var elasticsearch = require('elasticsearch');

var elasticSearchClient = new elasticsearch.Client()
// var elasticSearchClient = new ElasticSearchClient(serverOptions);

var _index = "codecollection";
var _type = 'javaFiles';

// Configuration

app.configure(function () {
    app.set('views', __dirname + '/views');
    app.set('view engine', 'jade');
    app.use(express.bodyParser());
    app.use(express.methodOverride());
    app.use(app.router);
    app.use(express.static(__dirname + '/public'));
});

app.configure('development', function () {
    app.use(express.errorHandler({ dumpExceptions:true, showStack:true }));
});

app.configure('production', function () {
    app.use(express.errorHandler());
});

// Routes
app.get('/', function (req, res) {
    elasticSearchClient.ping({
        requestTimeout: 3000,
    }, function (error) {
    if (error) {
        res.render('asearch',{result:"Error: connect ECONNREFUSED"});
    } else {
        res.render('asearch',{result:""});
    }
});
});

app.get('/advance', function (req, res) {
    elasticSearchClient.ping({
        requestTimeout: 3000,
    }, function (error) {
    if (error) {
        res.render('advance',{result:"Error: connect ECONNREFUSED"});
    } else {
        res.render('advance',{result:""});
    }
});
});


app.get('/asearch', function (req, res) {
    elasticSearchClient.ping({
        requestTimeout: 3000,
    }, function (error) {
    if (error) {
        res.render('asearch',{result:"Error: connect ECONNREFUSED"});
    } else {
        res.render('asearch',{result:""});
    }
});
});

app.get('/show',function(req,res) {
    elasticSearchClient.get({
        "index":_index,
        "type":_type,
        "id": req.query.path,
    }, function(error, response){
        if(error){
            res.render('show', { result:error })
        }
        else{
            res.render('show', { result:response })
        }
    })
});


app.get('/advancesearch', function(req, res){
    var option = req.query.optionsRadiosinline;
    var class_name,class_modifier,class_extend,class_implement;
    var fun_name,fun_modifier,fun_input,fun_output;
    if (option==0) {
        var class_name = req.query.class_name;
        var class_modifier = req.query.class_modifier;
        var class_extend = req.query.class_extend;
        var class_implement = req.query.class_implement;
        // op= "must"
    }else {
        var fun_name = req.query.fun_name;
        var fun_modifier = req.query.fun_modifier;
        var fun_input = req.query.fun_input;
        var fun_output = req.query.fun_output;
        // op = "should"
    }
    // var claas_name = req.query.class_name;
    // var class_modifier = req.query.class_modifier;
    // var class_extend = req.query.class_extend;
    // var class_implement = req.query.class_implement;
    // var fun_name = req.query.fun_name;
    // var fun_modifier = req.query.fun_modifier;
    // var fun_input = req.query.fun_input;
    // var fun_output = req.query.fun_output;
    var op = "";

   
    func_qryObj = []
    if(fun_name!=""){
        tmpjson = {
            "match":{
                "defined_fun.fun_name":fun_name
            }
        }
        func_qryObj.push(tmpjson)
    }
    if(fun_modifier!=""){
        tmpjson = {
            "match":{
                "defined_fun.fun_modifier":fun_modifier
            }
        }
        func_qryObj.push(tmpjson)
    }
    if(fun_input!=""){
        tmpjson = {
            "nested":{
                "path":"defined_fun.fun_input",
                "query":{
                    "match":{
                        "defined_fun.fun_input.input_type":fun_input
                    }
                }
            }
        }
        func_qryObj.push(tmpjson)
    }
    if(fun_output!=""){
        tmpjson = {
            "match":{
                "defined_fun.fun_return":fun_output
            }
        }
        func_qryObj.push(tmpjson)
    }

    class_qryObj = []
    if(class_name!=""){
        tmpjson = {
            "match":{
                "defined_class.class_name":class_name
            }
        }
        class_qryObj.push(tmpjson)
    }
    if(class_modifier!=""){
        tmpjson = {
            "match":{
                "defined_class.class_modifier":class_modifier
            }
        }
        class_qryObj.push(tmpjson)
    }
    if(class_extend!=""){
        tmpjson = {
            "match":{
                "defined_class.class_extend":class_extend
            }
        }
        class_qryObj.push(tmpjson)
    }
    if(class_implement!=""){
        tmpjson = {
            "match":{
                "defined_class.class_implement":class_implement
            }
        }
        class_qryObj.push(tmpjson)
    }
    var body;
    var path="";
    if (option==0) {
        body = class_qryObj;
        path="defined_class"
    }else{
        body = func_qryObj;
        path="defined_fun"
    }
    console.log(body)
    var qryObj2 = {
                    "query":{
                                "nested":
                                {
                                    "path":path,
                                    "query":{
                                        "bool":{
                                            "must":body
                                        }
                                    }

                                }
                            }
            };

    var qryObj = {
                "query":{
                    "bool":{
                    [op]:[
                        {
                            "nested":
                            {
                                "path":"defined_fun",
                                "query":{
                                    "bool":{
                                        "must":func_qryObj
                                    }
                                }

                            }
                        },
                        {
                            "nested":
                            {
                                "path":"defined_class",
                                "query":{
                                    "bool":{
                                        "must":class_qryObj
                                    }
                                }

                            }
                        }
                    ]
                }
                }   
        };
    console.log(qryObj2);

    elasticSearchClient.search({
        "index":_index, 
        "type":_type,
        "size": 20,
        "from":req.query.s,
        "body":qryObj2
    }, function(error, response){
        if (error){
            res.render('searchr', { result:error })
        }else{
           var data = response;
           var length = Math.floor(response.hits.total/20);
           if (response.hits.total > 20)
                count = 20
            else
                count = response.hits.total 
           for(var i=0;i<count;i++){
                data.hits.hits[i]["_source"]['showurl'] = "/show?path="+response.hits.hits[i]["_id"];
           }
           var indexurl=[];
           if (length >=10)
                length = 10;
           for (var i=0;i<length;i++){
                var tmp={}
                req.query.s=(i*20).toString();
                var tmpstr = url.parse(req.url).query
                tmp['url'] = "/advancesearch?"+tmpstr+"&s="+(i*20).toString()
                tmp['index'] = i+1;
                indexurl.push(tmp)
           }
           data['urls']=indexurl
           res.render('searchr', { result:data})
        }
    });

});

app.get('/search', function (req, res) {
    var qryObj = {
            // "nested":{
                // "path":"defined_fun",
                "query":{
                    "match":{
                        "_all":req.query.q
                    }
                // }
                
            }   
    };
    elasticSearchClient.search({
        "index":_index, 
        "type":_type,
        "size": 20,
        "from":req.query.s,
        "body":qryObj
    }, function(error, response){
        if (error){
            res.render('searchr', { result:error })
        }else{
           var data = response;
           var length = Math.floor(response.hits.total/20);
           if (response.hits.total > 20)
                count = 20
            else
                count = response.hits.total 
           for(var i=0;i<count;i++){
                data.hits.hits[i]["_source"]['showurl'] = "/show?path="+response.hits.hits[i]["_id"];
           }
           var indexurl=[];
           if (length >=10)
                length = 10;
           for (var i=0;i<length;i++){
                var tmp={}
                tmp['url'] = "/search?q="+req.query.q+"&s="+(i*20).toString()
                tmp['index'] = i+1;
                indexurl.push(tmp)
           }
           data['urls']=indexurl
           res.render('searchr', { result:data})
        }
    });
    // }).on('data',
    //     function (data) {
    //         res.render('search', { result:JSON.parse(data)})
    //     }).on('error', function (error) {
    //         res.render('search', { result:error })
    //     })
    //     .exec()

});


var port = process.env.PORT || 3000;

app.listen(port, function () {
    console.log("Express server listening on port %d in %s mode", app.address().port, app.settings.env);
});
