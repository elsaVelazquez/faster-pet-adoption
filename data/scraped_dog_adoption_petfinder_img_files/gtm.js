
// Copyright 2012 Google Inc. All rights reserved.
(function(w,g){w[g]=w[g]||{};w[g].e=function(s){return eval(s);};})(window,'google_tag_manager');(function(){

var data = {
"resource": {
  "version":"284",
  
  "macros":[{
      "function":"__u",
      "vtp_component":"HOST",
      "vtp_enableMultiQueryKeys":false,
      "vtp_enableIgnoreEmptyQueryParam":false
    },{
      "function":"__e"
    },{
      "function":"__v",
      "vtp_name":"gtm.triggers",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":""
    },{
      "function":"__c",
      "vtp_value":"UA-34990229-2"
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",0],
      "vtp_fullMatch":false,
      "vtp_replaceAfterMatch":false,
      "vtp_ignoreCase":true,
      "vtp_defaultValue":"catch all",
      "vtp_map":["list",["map","key","^(.*\\.|)purina\\.com","value","purina.com"],["map","key","^(.*\\.|)tidycats\\.com","value","tidy cats"],["map","key","^(.*\\.|)purinatreats\\.com","value","treats"],["map","key","^(.*\\.|)purinapack\\.purina\\.com","value","purina pack"],["map","key","^(.*\\.|)dogchow\\.com","value","dog chow"],["map","key","^(.*\\.|)(purina(one|)beyond|beyondpetfood|trybeyondnow)\\.com","value","beyond"],["map","key","^(.*\\.|)purinaproclub\\.com","value","purina pro club"],["map","key","^www\\.purinainstitute\\.com","value","purina institute"],["map","key","^(.*\\.|)petfinder\\.com","value","petfinder"],["map","key","^(.*\\.|)growingpupapp\\.com","value","growing pup"],["map","key","((?:nestle)?purina(?:careers|jobs)\\.com|nestleusa\\.taleo\\.net|applytracking.com|nestletechcareers\\.com)","value","careers"],["map","key","^(.*\\.|)proplanvetdirect\\.com","value","pro plan vet direct"],["map","key","^(.*\\.|)purinashelterchampions\\.com","value","purina shelter champions"],["map","key","{\"gap\":\"UA-34990229-35\", \"gtm\":\"GTM-5QCDLK9\", \"lytics\":\"1\", \"nestleID\":\"Purina For Professionals\", \"nestleDiGiPi\":\"872\"}","value","p4p"],["map","key","\/^((.*\\.|)purinastore|store\\.purina)\\.com\/i","value","purina store"],["map","key","^(.*\\.|)petsupportalliance\\.com","value","pet support alliance"],["map","key","^(.*\\.|)petqcheck\\.com","value","petqcheck"],["map","key","^(.*\\.|)reducecatallergens\\.com","value","reduce cat allergens"],["map","key","^(.*\\.|)purinaproplanvets\\.com","value","purina pro plan vets"]]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",4],
      "vtp_name":"siteID"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return\"\"===",["escape",["macro",5],8,16],"||\"master\"===",["escape",["macro",5],8,16],"?",["escape",["macro",4],8,16],":",["escape",["macro",5],8,16],"})();"]
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",0],
      "vtp_fullMatch":false,
      "vtp_replaceAfterMatch":false,
      "vtp_defaultValue":["macro",6],
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key","(^|\\.|\\-)(?!(stage\\.fb\\.proplan))((local|qa|stage|dev|ansiradigital|ansira\\.purina|uspurina\\.acsitefactory|bvdev|preview\\.arcww2|alpha|beta|azure|test|test-site|staging|prod|int\\.|preprod)[^\\.]*)","value","dev and qa"]]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){var c=[\"",["escape",["macro",3],7],"\"],d=\"_ga_originalSendHitTask\";return function(a){window[d]=window[d]||a.get(\"sendHitTask\");a.set(\"sendHitTask\",function(b){var a=b,e=window[d],f=!0;try{if(f\u0026\u0026e(b),\"undefined\"!==typeof c\u0026\u0026c.length\u0026\u0026\"petfinder\"!==",["escape",["macro",7],8,16],"\u0026\u0026\"catch all\"!==",["escape",["macro",7],8,16],"\u0026\u0026\"dev and qa\"!==",["escape",["macro",7],8,16],"){var g=b.get(\"hitPayload\"),h=new RegExp(b.get(\"trackingId\"),\"gi\");c.forEach(function(a){b.set(\"hitPayload\",g.replace(h,a),!0);f\u0026\u0026e(b)})}}catch(k){e(a)}})}})();"]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":1,
      "vtp_setDefaultValue":false,
      "vtp_name":"ecommerce"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){var a=JSON.parse(JSON.stringify(",["escape",["macro",9],8,16],"));return{ecommerce:a}})();"]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"page"
    },{
      "function":"__f",
      "vtp_component":"URL"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",12],8,16],".replace(\/(.+?)((?:f|l)(?:irst|ast)?.?name)(=|\\-|_)([^\u0026\\\/]+)\/gi,\"$1$2$3[redacted]\")})();"]
    },{
      "function":"__remm",
      "vtp_setDefaultValue":false,
      "vtp_input":["macro",13],
      "vtp_fullMatch":true,
      "vtp_replaceAfterMatch":true,
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key","(.*\/\/[^\\?\\#]*).*","value","$1"]]
    },{
      "function":"__c",
      "vtp_value":"^(.*)(=|\\\/)([A-Za-z0-9._%+-]+(\\%40|@)[A-Za-z0-9.-]+\\.[A-Za-z]{2,4})(.*)$"
    },{
      "function":"__c",
      "vtp_value":"$1$2[redacted]$5"
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",14],
      "vtp_fullMatch":true,
      "vtp_replaceAfterMatch":true,
      "vtp_defaultValue":["macro",14],
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key",["macro",15],"value",["macro",16]]]
    },{
      "function":"__u",
      "vtp_component":"URL",
      "vtp_enableMultiQueryKeys":false,
      "vtp_enableIgnoreEmptyQueryParam":false
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",18],8,16],".replace(\/(.+?)((?:f|l)(?:irst|ast)?.?name)(=|\\-|_)([^\u0026\\\/]+)\/gi,\"$1$2$3[redacted]\")})();"]
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",19],
      "vtp_fullMatch":true,
      "vtp_replaceAfterMatch":true,
      "vtp_defaultValue":["macro",19],
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key",["macro",15],"value",["macro",16]]]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"eventCallback"
    },{
      "function":"__j",
      "vtp_name":"document.title"
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",22],
      "vtp_fullMatch":true,
      "vtp_replaceAfterMatch":true,
      "vtp_defaultValue":["macro",22],
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key","^(.+\\sfile\\s\\\")([^\\\"]+)(\\\".+)","value","$1[redacted]$3"]]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"metrics"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",24],8,16],")[0]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",24],8,16],"[Object.keys(",["escape",["macro",24],8,16],")[0]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",24],8,16],")[1]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",24],8,16],"[Object.keys(",["escape",["macro",24],8,16],")[1]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",24],8,16],")[2]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",24],8,16],"[Object.keys(",["escape",["macro",24],8,16],")[2]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",24],8,16],")[3]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",24],8,16],"[Object.keys(",["escape",["macro",24],8,16],")[3]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",24],8,16],")[4]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",24],8,16],"[Object.keys(",["escape",["macro",24],8,16],")[4]]||\"\"})();"]
    },{
      "function":"__u",
      "vtp_component":"QUERY",
      "vtp_queryKey":"icid",
      "vtp_enableMultiQueryKeys":false,
      "vtp_enableIgnoreEmptyQueryParam":false
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"dimensions"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[0]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[0]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[1]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[1]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[2]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[2]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[3]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[3]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[4]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[4]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[5]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[5]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[6]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[6]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[7]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[7]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[8]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[8]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[9]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[9]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[10]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[10]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[11]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[11]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[12]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[12]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[13]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[13]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[14]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[14]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[15]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[15]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[16]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[16]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[17]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[17]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[18]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[18]]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return Object.keys(",["escape",["macro",36],8,16],")[19]||\"\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",36],8,16],"[Object.keys(",["escape",["macro",36],8,16],")[19]]||\"\"})();"]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"language"
    },{
      "function":"__k",
      "vtp_decodeCookie":false,
      "vtp_name":"IDR_AnsiraID"
    },{
      "function":"__c",
      "vtp_value":"gtm"
    },{
      "function":"__smm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",7],
      "vtp_defaultValue":"{\"gap\":\"UA-34990229-56\"}",
      "vtp_map":["list",["map","key","catch all","value","{\"gap\":\"UA-34990229-56\", \"lytics\":\"1\"}"],["map","key","dev and qa","value","{\"gap\":\"UA-34990229-57\", \"lytics\":\"1\", \"nestleID\":\"Purina Dev Site\", \"nestleDiGiPi\":\"00000\"}"],["map","key","purina.com","value","{\"gap\":\"UA-34990229-3\", \"gtm\":\"GTM-KBH7G46\", \"bk\":\"38366\", \"lytics\":\"1\", \"nestleID\":\"Purina 1\", \"nestleDiGiPi\":\"827\"}"],["map","key","tidy cats","value","{\"gap\":\"UA-34990229-24\", \"gtm\":\"GTM-K2FVF4R\", \"bk\":\"23571\", \"lytics\":\"1\", \"nestleID\":\"Tidy Cats\", \"nestleDiGiPi\":\"999\"}"],["map","key","treats","value","{\"gap\":\"UA-34990229-79\", \"gtm\":\"GTM-5H36ZVD\", \"bk\":\"52527\", \"lytics\":\"1\", \"nestleID\":\"Purina Treats\", \"nestleDiGiPi\":\"65622\"}"],["map","key","purina pack","value","{\"gap\":\"UA-37239183-62\"}"],["map","key","purina pro club","value","{\"gap\":\"UA-34990229-27\", \"gtm\":\"GTM-T54K2DR\", \"bk\":\"63738\", \"nestleID\":\"Pro Club\", \"nestleDiGiPi\":\"909\"}"],["map","key","petfinder","value","{\"gap\":\"UA-6568435-1\", \"gtm\":\"GTM-P6ZVL6X\", \"bk\":\"24955\", \"lytics\":\"1\", \"nestleID\":\"Petfinder\", \"nestleDiGiPi\":\"4617\", \"nestleTechnology\":\"PHP\"}"],["map","key","purina institute","value","{\"gap\":\"UA-34990229-80\", \"bk\":\"63355\", \"nestleID\":\"Purina Institute\", \"nestleDiGiPi\":\"49081\"}"],["map","key","growing pup","value","{\"gap\":\"UA-129306867-4\", \"nestleID\":\"Growing Pup App\", \"nestleDiGiPi\":\"67861\", \"nestleType\":\"App\", \"nestleTechnology\":\"Umbraco\"}"],["map","key","just right","value","{\"gap\":\"UA-37239183-33\", \"gtm\":\"GTM-TC5R6F5\", \"bk\":\"48146\", \"lytics\":\"1\", \"nestleID\":\"Just Right Pet Food\", \"nestleDiGiPi\":\"7416\", \"nestleProperties\":\"e-commerce\"}"],["map","key","purina store","value","{\"gap\":\"UA-34990229-31\", \"gtm\":\"GTM-PKG69L9\", \"bk\":\"55920\", \"lytics\":\"1\", \"nestleID\":\"Purina Store\", \"nestleDiGiPi\":\"62847\", \"nestleProperties\":\"e-commerce\"}"],["map","key","careers","value","{\"gap\":\"UA-34990229-11\", \"gtm\":\"GTM-TQ4LBCD\", \"bk\":\"51895\", \"nestleID\":\"Purina Careers\", \"nestleDiGiPi\":\"66126\"}"],["map","key","pro plan vet direct","value","{\"gap\":\"UA-34990229-74\", \"gtm\":\"GTM-PR9L6H2\", \"bk\":\"48128\", \"lytics\":\"1\", \"nestleID\":\"Pro Plan Vet Direct\", \"nestleDiGiPi\":\"55096\"}"],["map","key","purina shelter champions","value","{\"gap\":\"UA-37239183-46\", \"gtm\":\"GTM-K9W4FWB\", \"nestleID\":\"Purina Shelter Champions\", \"nestleDiGiPi\":\"34883\"}"],["map","key","p4p","value","{\"gap\":\"UA-34990229-35\", \"gtm\":\"GTM-5QCDLK9\", \"lytics\":\"1\", \"nestleID\":\"Purina For Professionals\", \"nestleDiGiPi\":\"872\"}"],["map","key","pet support alliance","value","{\"gap\":\"UA-129306867-36\", \"nestleID\":\"Pet Support Alliance\", \"nestleDiGiPi\":\"72352\"}"],["map","key","petqcheck","value","{\"gap\":\"UA-129306867-31\", \"nestleID\":\"PetQCheck\", \"nestleDiGiPi\":\"72072\"}"],["map","key","reduce cat allergens","value","{\"gap\":\"UA-129306867-37\", \"nestleID\":\"Reduce Cat Allergens\", \"nestleDiGiPi\":\"72130\"}"],["map","key","purina pro plan vets","value","{\"gap\":\"UA-34990229-73\", \"gtm\":\"GTM-5GHM26T\", \"bk\":\"59904\", \"lytics\":\"1\", \"nestleID\":\"Purina Pro Plan Vets\", \"nestleDiGiPi\":\"53630\"}"]]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").nestleType||\"Site\"})();"]
    },{
      "function":"__smm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",81],
      "vtp_defaultValue":"website",
      "vtp_map":["list",["map","key","Site","value","website"],["map","key","App","value","mobile app"]]
    },{
      "function":"__v",
      "convert_case_to":1,
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"pageTemplate"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"content_type"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",84],
      "vtp_name":"contentType"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"page_brand"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",86],
      "vtp_name":"pageBrand"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"page_pet_age"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",88],
      "vtp_name":"pagePetAge"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"page_pet_type"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",90],
      "vtp_name":"pagePetType"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"page_type"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",92],
      "vtp_name":"pageType"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"page_product_functional_health"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",94],
      "vtp_name":"pageProductFunctionalHealth"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"page_product_type"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",96],
      "vtp_name":"pageProductType"
    },{
      "function":"__gas",
      "vtp_useDebugVersion":false,
      "vtp_useHashAutoLink":false,
      "vtp_autoLinkDomains":"profiles.purina.com",
      "vtp_decorateFormsAutoLink":false,
      "vtp_cookieDomain":"auto",
      "vtp_useEcommerceDataLayer":false,
      "vtp_ecommerceMacroData":["macro",10],
      "vtp_doubleClick":false,
      "vtp_setTrackerName":false,
      "vtp_fieldsToSet":["list",["map","fieldName","allowLinker","value","true"],["map","fieldName","cookieName","value","ga_vid"],["map","fieldName","page","value",["macro",11]],["map","fieldName","anonymizeIp","value","true"],["map","fieldName","referrer","value",["macro",17]],["map","fieldName","location","value",["macro",20]],["map","fieldName","eventCallback","value",["macro",21]],["map","fieldName","title","value",["macro",23]]],
      "vtp_metric":["list",["map","index",["macro",25],"metric",["macro",26]],["map","index",["macro",27],"metric",["macro",28]],["map","index",["macro",29],"metric",["macro",30]],["map","index",["macro",31],"metric",["macro",32]],["map","index",["macro",33],"metric",["macro",34]]],
      "vtp_enableLinkId":false,
      "vtp_dimension":["list",["map","index","10","dimension",["macro",35]],["map","index","11","dimension",["macro",35]],["map","index",["macro",37],"dimension",["macro",38]],["map","index",["macro",39],"dimension",["macro",40]],["map","index",["macro",41],"dimension",["macro",42]],["map","index",["macro",43],"dimension",["macro",44]],["map","index",["macro",45],"dimension",["macro",46]],["map","index",["macro",47],"dimension",["macro",48]],["map","index",["macro",49],"dimension",["macro",50]],["map","index",["macro",51],"dimension",["macro",52]],["map","index",["macro",53],"dimension",["macro",54]],["map","index",["macro",55],"dimension",["macro",56]],["map","index",["macro",57],"dimension",["macro",58]],["map","index",["macro",59],"dimension",["macro",60]],["map","index",["macro",61],"dimension",["macro",62]],["map","index",["macro",63],"dimension",["macro",64]],["map","index",["macro",65],"dimension",["macro",66]],["map","index",["macro",67],"dimension",["macro",68]],["map","index",["macro",69],"dimension",["macro",70]],["map","index",["macro",71],"dimension",["macro",72]],["map","index",["macro",73],"dimension",["macro",74]],["map","index",["macro",75],"dimension",["macro",76]],["map","index","39","dimension",["macro",77]],["map","index","22","dimension",["macro",78]],["map","index","23","dimension",["macro",79]],["map","index","24","dimension",["macro",82]],["map","index","103","dimension",["macro",83]],["map","index","72","dimension",["macro",85]],["map","index","106","dimension",["macro",87]],["map","index","107","dimension",["macro",89]],["map","index","108","dimension",["macro",91]],["map","index","109","dimension",["macro",93]],["map","index","110","dimension",["macro",95]],["map","index","111","dimension",["macro",97]]],
      "vtp_enableEcommerce":true,
      "vtp_trackingId":"UA-34990229-56",
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_ecommerceIsEnabled":true
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").gap})();"]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":"0",
      "vtp_name":"nonInteraction"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"eventValue"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"eventCategory"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"eventAction"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":"(not set)",
      "vtp_name":"eventLabel"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").nestleCountry||\"United States\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").nestleID+\" \"+",["escape",["macro",105],8,16],"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return(\"\/ams\/\"+",["escape",["macro",105],8,16],"+\"\/\"+",["escape",["macro",106],8,16],").toLowerCase()})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").nestleProperties||\"Brand\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").nestleTechnology||\"Acquia\"})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").nestleDiGiPi})();"]
    },{
      "function":"__c",
      "vtp_value":"UA-34990229-78"
    },{
      "function":"__c",
      "vtp_value":"UA-27534376-1"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return\"dev and qa\"===",["escape",["macro",7],8,16],"?",["escape",["macro",111],8,16],":",["escape",["macro",112],8,16],"})();"]
    },{
      "function":"__gas",
      "vtp_cookieDomain":"auto",
      "vtp_doubleClick":false,
      "vtp_setTrackerName":false,
      "vtp_useDebugVersion":false,
      "vtp_fieldsToSet":["list",["map","fieldName","page","value",["macro",107]],["map","fieldName","anonymizeIp","value","true"],["map","fieldName","referrer","value",["macro",17]],["map","fieldName","location","value",["macro",20]],["map","fieldName","title","value",["macro",23]]],
      "vtp_useHashAutoLink":false,
      "vtp_autoLinkDomains":"profiles.purina.com",
      "vtp_decorateFormsAutoLink":false,
      "vtp_enableLinkId":false,
      "vtp_dimension":["list",["map","index","1","dimension","AMS"],["map","index","2","dimension",["macro",105]],["map","index","3","dimension","Petcare"],["map","index","4","dimension","Purina"],["map","index","5","dimension",["macro",106]],["map","index","6","dimension",["macro",108]],["map","index","7","dimension",["macro",81]],["map","index","8","dimension",["macro",0]],["map","index","9","dimension","English"],["map","index","10","dimension",["macro",109]],["map","index","12","dimension",["macro",110]]],
      "vtp_enableEcommerce":false,
      "vtp_trackingId":["macro",113],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"socialAction"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"socialTarget"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"socialNetwork"
    },{
      "function":"__u",
      "vtp_component":"PATH",
      "vtp_enableMultiQueryKeys":false,
      "vtp_enableIgnoreEmptyQueryParam":false
    },{
      "function":"__remm",
      "vtp_setDefaultValue":false,
      "vtp_input":["macro",118],
      "vtp_fullMatch":false,
      "vtp_replaceAfterMatch":false,
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key","^\\\/muse\\\/?","value","muse"],["map","key","^\\\/(cat-chow)\\\/?","value","cat-chow"],["map","key","^\\\/(purina-one)\\\/?","value","purina-one"],["map","key","^\\\/(pioneer-woman)\\\/?","value","pioneer-woman"],["map","key","^\\\/busy\\\/?","value","busy"],["map","key","^\\\/friskies\\\/?","value","friskies"],["map","key","^\\\/dog-chow\\\/?","value","dog-chow"],["map","key","^\\\/pro-plan\\\/?","value","pro-plan"],["map","key","^\\\/beneful\\\/?","value","beneful"],["map","key","^\\\/beyond\\\/?","value","beyond"],["map","key","^\\\/bella\\\/?","value","bella"],["map","key","^\\\/mighty-dog\\\/?","value","mighty-dog"],["map","key","^\\\/alpo\\\/?","value","alpo"],["map","key","^\\\/waggin-train\\\/?","value","waggin-train"],["map","key","^\\\/beggin\\\/?","value","beggin"],["map","key","^\\\/tidy-cats\\\/?","value","tidy-cats"],["map","key","^\\\/yesterdays-news\\\/?","value","yesterdays-news"],["map","key","^\\\/fancy-feast\\\/?","value","fancy-feast"]]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",119],
      "vtp_name":"brandID"
    },{
      "function":"__uv"
    },{
      "function":"__smm",
      "convert_case_to":1,
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",120],
      "vtp_defaultValue":["macro",120],
      "vtp_map":["list",["map","key","(not set)","value",["macro",119]],["map","key",["macro",121],"value",["macro",119]]]
    },{
      "function":"__smm",
      "vtp_setDefaultValue":false,
      "vtp_input":["macro",122],
      "vtp_map":["list",["map","key","muse","value","{\"gap\":\"UA-34990229-68\", \"regex\":\"\\\/muse\\\/?\"}"],["map","key","cat-chow","value","{\"gap\":\"UA-34990229-12\", \"regex\":\"\\\/(cat-chow)\\\/?\"}"],["map","key","purina-one","value","{\"gap\":\"UA-34990229-29\", \"regex\":\"\\\/(purina-one)\\\/?\"}"],["map","key","pioneer-woman","value","{\"gap\":\"UA-129306867-9\", \"regex\":\"\\\/pioneer-woman\\\/?\"}"],["map","key","busy","value","{\"gap\":\"UA-129306867-8\", \"regex\":\"\\\/busy\\\/?\"}"],["map","key","friskies","value","{\"gap\":\"UA-34990229-19\", \"regex\":\"\\\/friskies\\\/?\"}"],["map","key","dog-chow","value","{\"gap\":\"UA-34990229-15\", \"regex\":\"\\\/dog-chow\\\/?\"}"],["map","key","pro-plan","value","{\"gap\":\"UA-34990229-28\", \"regex\":\"\\\/pro-plan\\\/?\"}"],["map","key","dentalife","value","{\"gap\":\"UA-129306867-11\", \"regex\":\"\\\/dentalife\\\/?\"}"],["map","key","beneful","value","{\"gap\":\"UA-34990229-8\", \"regex\":\"\\\/beneful\\\/?\"}"],["map","key","beyond","value","{\"gap\":\"UA-34990229-65\", \"regex\":\"\\\/beyond\\\/?\"}"],["map","key","bella","value","{\"gap\":\"UA-34990229-75\", \"regex\":\"\\\/bella\\\/?\"}"],["map","key","mighty-dog","value","{\"gap\":\"UA-34990229-25\", \"regex\":\"\\\/mighty-dog\\\/?\"}"],["map","key","alpo","value","{\"gap\":\"UA-34990229-5\", \"regex\":\"\\\/alpo\\\/?\"}"],["map","key","waggin-train","value","{\"gap\":\"UA-129306867-18\", \"regex\":\"\\\/waggin-train\\\/?\"}"],["map","key","beggin","value","{\"gap\":\"UA-129306867-19\", \"regex\":\"\\\/beggin\\\/?\"}"],["map","key","tidy-cats","value","{\"gap\":\"UA-34990229-24\", \"regex\":\"\\\/tidy-cats\\\/?\"}"],["map","key","yesterdays-news","value","{\"gap\":\"UA-37239183-15\", \"regex\":\"\\\/yesterdays-news\\\/?\"}"],["map","key","fancy-feast","value","{\"gap\":\"UA-34990229-17\", \"regex\":\"\\\/fancy-feast\\\/?\"}"]]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",123],8,16],").regex})();"]
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",12],
      "vtp_fullMatch":false,
      "vtp_replaceAfterMatch":false,
      "vtp_defaultValue":["macro",17],
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key",["template","purina\\.com",["macro",124]],"value",""]]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",123],8,16],").gap})();"]
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",120],
      "vtp_fullMatch":true,
      "vtp_replaceAfterMatch":true,
      "vtp_defaultValue":["macro",6],
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key","(^(?!\\(not set\\)).+)*(cat\\-chow|muse|purina\\-one|friskies|beyond|bella|beneful|pro\\-plan|dog\\-chow)","value",["macro",120]]]
    },{
      "function":"__smm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",127],
      "vtp_defaultValue":"(not set)",
      "vtp_map":["list",["map","key","bella","value","count1"],["map","key","beneful","value","count2"],["map","key","beyond","value","count7"],["map","key","cat-chow","value","count12"],["map","key","dog-chow","value","count3"],["map","key","fancy feast","value","count4"],["map","key","muse","value","count5"],["map","key","purina pro club","value","count11"],["map","key","purina.com","value","count8"],["map","key","purina-one","value","count9"],["map","key","tidy cats","value","count10"],["map","key","pro-plan","value","count6"],["map","key","friskies","value","count0"],["map","key","petfinder","value","petfi0"],["map","key","careers","value","count17"],["map","key","pro plan vet direct","value","count18"],["map","key","p4p","value","count19"],["map","key","purina shelter champions","value","count20"],["map","key","purina store","value","count21"],["map","key","reduce cat allergens","value","count22"],["map","key","pet support alliance","value","count23"],["map","key","petqcheck","value","count24"]]
    },{
      "function":"__c",
      "vtp_value":["template",["macro",22]," | ",["macro",18]," | ",["macro",12]]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ga.getAll()[0].get(\"clientId\")})();"]
    },{
      "function":"__r"
    },{
      "function":"__u",
      "vtp_enableMultiQueryKeys":false,
      "vtp_enableIgnoreEmptyQueryParam":false
    },{
      "function":"__aev",
      "vtp_setDefaultValue":false,
      "vtp_stripWww":false,
      "vtp_varType":"URL",
      "vtp_component":"HOST"
    },{
      "function":"__smm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",133],
      "vtp_defaultValue":"true",
      "vtp_map":["list",["map","key",["macro",0],"value","false"]]
    },{
      "function":"__aev",
      "vtp_setDefaultValue":false,
      "vtp_varType":"URL",
      "vtp_component":"PATH",
      "vtp_defaultPages":["list"]
    },{
      "function":"__c",
      "vtp_value":["template",["macro",133],["macro",135]]
    },{
      "function":"__v",
      "vtp_name":"gtm.elementUrl",
      "vtp_dataLayerVersion":1
    },{
      "function":"__u",
      "vtp_component":"EXTENSION",
      "vtp_customUrlSource":["macro",137],
      "vtp_enableMultiQueryKeys":false,
      "vtp_enableIgnoreEmptyQueryParam":false
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){var a=\"",["escape",["macro",137],7],"\".match(\/[^\/\\\\\u0026\\?]+\\.\\w{3,4}(?=([\\?\u0026].*$|$))\/);return a instanceof Array?a[0]:void 0})();"]
    },{
      "function":"__dbg"
    },{
      "function":"__smm",
      "vtp_setDefaultValue":false,
      "vtp_input":["macro",0],
      "vtp_map":["list",["map","key","mypupapp.com","value","G-86EL1D8CVY"],["map","key","mypupapp.uspurina.acsitefactory.com","value","G-4B2EJJEBB0"]]
    },{
      "function":"__cid"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").bk})();"]
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return JSON.parse(",["escape",["macro",80],8,16],").lytics})();"]
    },{
      "function":"__aev",
      "vtp_setDefaultValue":false,
      "vtp_varType":"ATTRIBUTE",
      "vtp_attribute":"data-virtualPageView"
    },{
      "function":"__jsm",
      "vtp_javascript":["template","(function(){return ",["escape",["macro",145],8,16],"?\"",["escape",["macro",145],7],"\".toLowerCase()+\"\/virtualpageview\".replace(\"\/\/virtualpageview\",\"\/virtualpageview\"):\"\"})();"]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":"false",
      "vtp_name":"acoe_loaded"
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",0],
      "vtp_fullMatch":false,
      "vtp_replaceAfterMatch":false,
      "vtp_defaultValue":"https:\/\/profiles.purina.com\/udc\/widget\/main.js",
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key","^dev\\.","value","https:\/\/qa-purinareg.ansiradigital.com\/udc\/widget\/main.js"],["map","key","^(test|preprod)\\.","value","https:\/\/uat-purinareg.ansiradigital.com\/udc\/widget\/main.js"]]
    },{
      "function":"__c",
      "vtp_value":["template",["macro",102],"|",["macro",103],"|",["macro",104]]
    },{
      "function":"__v",
      "vtp_name":"gtm.scrollThreshold",
      "vtp_dataLayerVersion":1
    },{
      "function":"__v",
      "vtp_name":"gtm.videoStatus",
      "vtp_dataLayerVersion":1
    },{
      "function":"__v",
      "vtp_name":"gtm.videoPercent",
      "vtp_dataLayerVersion":1
    },{
      "function":"__smm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",151],
      "vtp_defaultValue":["macro",151],
      "vtp_map":["list",["map","key","start","value","started"],["map","key","pause","value","paused"],["map","key","progress","value",["template",["macro",152],"% viewed"]]]
    },{
      "function":"__v",
      "vtp_name":"gtm.videoUrl",
      "vtp_dataLayerVersion":1
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",154],
      "vtp_fullMatch":true,
      "vtp_replaceAfterMatch":true,
      "vtp_defaultValue":"(no video id)",
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key",".+v\\=([^\\\u0026]+)","value","$1"]]
    },{
      "function":"__v",
      "vtp_name":"gtm.videoTitle",
      "vtp_dataLayerVersion":1
    },{
      "function":"__c",
      "convert_case_to":1,
      "vtp_value":["template",["macro",155]," - ",["macro",156]]
    },{
      "function":"__remm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",0],
      "vtp_fullMatch":false,
      "vtp_replaceAfterMatch":false,
      "vtp_defaultValue":"https:\/\/identity.ansira.com\/stat\/purinacore.js",
      "vtp_ignoreCase":true,
      "vtp_map":["list",["map","key","^(www\\-qa|test|stage)\\.","value","https:\/\/identity-qa.ansira.com\/stat\/purinacore.js"]]
    },{
      "function":"__c",
      "vtp_value":"4274e8ad322ec51d773bcb674ad26d77"
    },{
      "function":"__c",
      "vtp_value":"bd0571c73c4f6ed4fbd260086cc1c318"
    },{
      "function":"__smm",
      "vtp_setDefaultValue":true,
      "vtp_input":["macro",7],
      "vtp_defaultValue":["macro",159],
      "vtp_map":["list",["map","key","dev and qa","value",["macro",160]],["map","key","catch all","value",["macro",160]]]
    },{
      "function":"__smm",
      "vtp_setDefaultValue":false,
      "vtp_input":["macro",7],
      "vtp_map":["list",["map","key","purina.com","value",["macro",122]]]
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userCity"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userState"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userZip"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userCountry"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetOwnership"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetType"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetAge"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetSize"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetGender"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetBreed"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetNumber"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetDietaryNeeds"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetName"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetSecondaryBreed"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetShelterName"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetShelterID"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetAcquisitionType"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"userPetBirthMonth"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfilePetID"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfilePetName"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileAnimalType"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileSpecies"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileAge"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileGender"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileSize"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfilePrimaryBreed"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileSecondaryBreed"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileMixedBreed"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfilePrimaryColor"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileCoatLength"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfilePetCharacteristics"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileGoodWith"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfilePetZipCode"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileShelterID"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileShelterName"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileArrivalDate"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfilePhotosInProfile"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileVideoPresent"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfileAdoptionFee"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"petProfilePetStatus"
    },{
      "function":"__k",
      "vtp_decodeCookie":false,
      "vtp_name":"widget_uuid"
    },{
      "function":"__k",
      "vtp_decodeCookie":false,
      "vtp_name":"purDebug"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"pageID"
    },{
      "function":"__u",
      "vtp_component":"QUERY",
      "vtp_queryKey":"utm_campaign",
      "vtp_enableMultiQueryKeys":false,
      "vtp_enableIgnoreEmptyQueryParam":false
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":false,
      "vtp_name":"page_template"
    },{
      "function":"__k",
      "vtp_decodeCookie":false,
      "vtp_name":"_evidon_consent_cookie"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":"none",
      "vtp_name":"evidonConsentGiven"
    },{
      "function":"__v",
      "vtp_dataLayerVersion":2,
      "vtp_setDefaultValue":true,
      "vtp_defaultValue":["macro",207],
      "vtp_name":"pageTemplate"
    },{
      "function":"__e"
    },{
      "function":"__hid"
    }],
  "tags":[{
      "function":"__paused",
      "vtp_originalTagType":"html",
      "tag_id":19
    },{
      "function":"__ua",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_overrideGaSettings":true,
      "vtp_fieldsToSet":["list",["map","fieldName","customTask","value",["macro",8]]],
      "vtp_trackType":"TRACK_PAGEVIEW",
      "vtp_gaSettings":["macro",98],
      "vtp_trackingId":["macro",99],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "tag_id":21
    },{
      "function":"__paused",
      "vtp_originalTagType":"ua",
      "tag_id":22
    },{
      "function":"__paused",
      "vtp_originalTagType":"ua",
      "tag_id":23
    },{
      "function":"__ua",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_nonInteraction":["macro",100],
      "vtp_overrideGaSettings":true,
      "vtp_eventValue":["macro",101],
      "vtp_fieldsToSet":["list",["map","fieldName","customTask","value",["macro",8]]],
      "vtp_eventCategory":["macro",102],
      "vtp_trackType":"TRACK_EVENT",
      "vtp_gaSettings":["macro",98],
      "vtp_eventAction":["macro",103],
      "vtp_eventLabel":["macro",104],
      "vtp_trackingId":["macro",99],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "vtp_trackTypeIsEvent":true,
      "tag_id":24
    },{
      "function":"__ua",
      "once_per_event":true,
      "vtp_overrideGaSettings":false,
      "vtp_trackType":"TRACK_PAGEVIEW",
      "vtp_gaSettings":["macro",114],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "tag_id":25
    },{
      "function":"__ua",
      "once_per_event":true,
      "vtp_nonInteraction":["macro",100],
      "vtp_overrideGaSettings":true,
      "vtp_eventValue":["macro",101],
      "vtp_eventCategory":["macro",102],
      "vtp_trackType":"TRACK_EVENT",
      "vtp_gaSettings":["macro",114],
      "vtp_eventAction":["macro",103],
      "vtp_eventLabel":["macro",104],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "vtp_trackTypeIsEvent":true,
      "tag_id":26
    },{
      "function":"__ua",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_overrideGaSettings":true,
      "vtp_fieldsToSet":["list",["map","fieldName","customTask","value",["macro",8]]],
      "vtp_trackType":"TRACK_SOCIAL",
      "vtp_socialAction":["macro",115],
      "vtp_gaSettings":["macro",98],
      "vtp_socialActionTarget":["macro",116],
      "vtp_socialNetwork":["macro",117],
      "vtp_trackingId":["macro",99],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "vtp_trackTypeIsSocial":true,
      "tag_id":29
    },{
      "function":"__paused",
      "vtp_originalTagType":"ua",
      "tag_id":30
    },{
      "function":"__ua",
      "once_per_event":true,
      "vtp_overrideGaSettings":true,
      "vtp_fieldsToSet":["list",["map","fieldName","referrer","value",["macro",125]],["map","fieldName","alwaysSendReferrer","value","true"]],
      "vtp_trackType":"TRACK_PAGEVIEW",
      "vtp_gaSettings":["macro",98],
      "vtp_trackingId":["macro",126],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "tag_id":46
    },{
      "function":"__ua",
      "once_per_event":true,
      "vtp_overrideGaSettings":true,
      "vtp_fieldsToSet":["list",["map","fieldName","referrer","value",["macro",125]],["map","fieldName","alwaysSendReferrer","value","true"]],
      "vtp_trackType":"TRACK_SOCIAL",
      "vtp_socialAction":["macro",115],
      "vtp_gaSettings":["macro",98],
      "vtp_socialActionTarget":["macro",116],
      "vtp_socialNetwork":["macro",117],
      "vtp_trackingId":["macro",126],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "vtp_trackTypeIsSocial":true,
      "tag_id":47
    },{
      "function":"__ua",
      "once_per_event":true,
      "vtp_nonInteraction":["macro",100],
      "vtp_overrideGaSettings":true,
      "vtp_eventValue":["macro",101],
      "vtp_fieldsToSet":["list",["map","fieldName","referrer","value",["macro",125]],["map","fieldName","alwaysSendReferrer","value","true"]],
      "vtp_eventCategory":["macro",102],
      "vtp_trackType":"TRACK_EVENT",
      "vtp_gaSettings":["macro",98],
      "vtp_eventAction":["macro",103],
      "vtp_eventLabel":["macro",104],
      "vtp_trackingId":["macro",126],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "vtp_trackTypeIsEvent":true,
      "tag_id":48
    },{
      "function":"__gclidw",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_enableCrossDomain":false,
      "vtp_enableCookieOverrides":false,
      "vtp_enableCrossDomainFeature":true,
      "vtp_enableCookieUpdateFeature":false,
      "vtp_enableCookieFlagsFeature":false,
      "vtp_enableUrlPassthroughFeature":false,
      "tag_id":53
    },{
      "function":"__flc",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_customVariable":["list",["map","key","u1","value",["macro",77]],["map","key","u2","value",["macro",127]],["map","key","u3","value",["macro",20]],["map","key","u4","value",["macro",22]],["map","key","u5","value",["macro",130]]],
      "vtp_enableConversionLinker":true,
      "vtp_groupTag":["macro",128],
      "vtp_useImageTag":true,
      "vtp_activityTag":"visitpv",
      "vtp_ordinalType":"STANDARD",
      "vtp_conversionCookiePrefix":"_gcl",
      "vtp_advertiserId":"9032298",
      "vtp_ordinalStandard":["macro",131],
      "vtp_url":["macro",132],
      "vtp_useImageTagIsTrue":true,
      "vtp_enableGoogleAttributionOptions":false,
      "vtp_showConversionLinkingControls":true,
      "tag_id":57
    },{
      "function":"__flc",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_customVariable":["list",["map","key","u1","value",["macro",77]],["map","key","u2","value",["macro",127]],["map","key","u3","value",["macro",20]],["map","key","u4","value",["macro",22]],["map","key","u5","value",["macro",130]]],
      "vtp_enableConversionLinker":true,
      "vtp_groupTag":["macro",128],
      "vtp_useImageTag":true,
      "vtp_activityTag":"landpv",
      "vtp_ordinalType":"UNIQUE",
      "vtp_conversionCookiePrefix":"_gcl",
      "vtp_advertiserId":"9032298",
      "vtp_ordinalUnique":"1",
      "vtp_number":["macro",131],
      "vtp_url":["macro",132],
      "vtp_useImageTagIsTrue":true,
      "vtp_enableGoogleAttributionOptions":false,
      "vtp_showConversionLinkingControls":true,
      "tag_id":58
    },{
      "function":"__flc",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_customVariable":["list",["map","key","u1","value",["macro",77]],["map","key","u2","value",["macro",127]],["map","key","u3","value",["macro",20]],["map","key","u4","value",["macro",22]],["map","key","u5","value",["macro",130]]],
      "vtp_enableConversionLinker":true,
      "vtp_groupTag":["macro",128],
      "vtp_useImageTag":true,
      "vtp_activityTag":"buynow",
      "vtp_ordinalType":"STANDARD",
      "vtp_conversionCookiePrefix":"_gcl",
      "vtp_advertiserId":"9032298",
      "vtp_ordinalStandard":["macro",131],
      "vtp_url":["macro",132],
      "vtp_useImageTagIsTrue":true,
      "vtp_enableGoogleAttributionOptions":false,
      "vtp_showConversionLinkingControls":true,
      "tag_id":59
    },{
      "function":"__flc",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_customVariable":["list",["map","key","u1","value",["macro",77]],["map","key","u2","value",["macro",127]],["map","key","u3","value",["macro",20]],["map","key","u4","value",["macro",22]],["map","key","u5","value",["macro",130]],["map","key","u7","value",["macro",127]]],
      "vtp_enableConversionLinker":true,
      "vtp_groupTag":["macro",128],
      "vtp_useImageTag":true,
      "vtp_activityTag":"couponev",
      "vtp_ordinalType":"STANDARD",
      "vtp_conversionCookiePrefix":"_gcl",
      "vtp_advertiserId":"9032298",
      "vtp_ordinalStandard":["macro",131],
      "vtp_url":["macro",132],
      "vtp_useImageTagIsTrue":true,
      "vtp_enableGoogleAttributionOptions":false,
      "vtp_showConversionLinkingControls":true,
      "tag_id":60
    },{
      "function":"__flc",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_customVariable":["list",["map","key","u1","value",["macro",77]],["map","key","u2","value",["macro",127]],["map","key","u3","value",["macro",20]],["map","key","u4","value",["macro",22]],["map","key","u5","value",["macro",130]]],
      "vtp_enableConversionLinker":true,
      "vtp_groupTag":["macro",128],
      "vtp_useImageTag":true,
      "vtp_activityTag":"singupev",
      "vtp_ordinalType":"SESSION",
      "vtp_sessionId":["macro",130],
      "vtp_conversionCookiePrefix":"_gcl",
      "vtp_advertiserId":"9032298",
      "vtp_ordinalIsSession":true,
      "vtp_url":["macro",132],
      "vtp_useImageTagIsTrue":true,
      "vtp_enableGoogleAttributionOptions":false,
      "vtp_showConversionLinkingControls":true,
      "tag_id":61
    },{
      "function":"__ua",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_nonInteraction":false,
      "vtp_overrideGaSettings":true,
      "vtp_fieldsToSet":["list",["map","fieldName","customTask","value",["macro",8]]],
      "vtp_eventCategory":"exit link",
      "vtp_trackType":"TRACK_EVENT",
      "vtp_gaSettings":["macro",98],
      "vtp_eventAction":"click",
      "vtp_eventLabel":["macro",136],
      "vtp_trackingId":["macro",99],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "vtp_trackTypeIsEvent":true,
      "tag_id":539
    },{
      "function":"__ua",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_nonInteraction":false,
      "vtp_overrideGaSettings":true,
      "vtp_fieldsToSet":["list",["map","fieldName","customTask","value",["macro",8]]],
      "vtp_eventCategory":"file download",
      "vtp_trackType":"TRACK_EVENT",
      "vtp_gaSettings":["macro",98],
      "vtp_eventAction":["macro",138],
      "vtp_eventLabel":["macro",139],
      "vtp_trackingId":["macro",99],
      "vtp_enableRecaptchaOption":false,
      "vtp_enableTransportUrl":false,
      "vtp_enableUaRlsa":false,
      "vtp_enableUseInternalVersion":false,
      "vtp_enableFirebaseCampaignData":true,
      "vtp_trackTypeIsEvent":true,
      "tag_id":544
    },{
      "function":"__gaawc",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_fieldsToSet":["list",["map","name","debug_mode","value",["macro",140]]],
      "vtp_sendPageView":true,
      "vtp_measurementId":["macro",141],
      "vtp_enableUserProperties":true,
      "tag_id":640
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-NP93C8Q","nickname","Brand - Muse"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"muse",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":647
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-KBH7G46","nickname","Site - Purina.com"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",7],"purina.com",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":648
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-P6ZVL6X","nickname","Site - Petfinder"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",5],"petfinder",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":649
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-WK2C2S9","nickname","Site - Cat Chow"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"cat-chow",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":650
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-5VF49F7","nickname","Site - Purina ONE"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"purina-one",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":651
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-MRSL5BW","nickname","Brand - Pioneer Woman"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"pioneer-woman",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":652
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-TNDFDFH","nickname","Brand - Busy"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"busy",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":653
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-MZ4K7RQ","nickname","Site - Friskies"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"friskies",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":654
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-PJ3GHFD","nickname","Site - Pro Plan"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"pro-plan",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":655
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-WGJNJMH","nickname","Site - Dog Chow"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"dog-chow",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":656
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-WN7LLGX","nickname","Site - Dentalife"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"dentalife",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":657
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-PKG69L9","nickname","Site - PurinaStore.com"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",6],"purina store",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":658
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-TC5R6F5","nickname","Site - JustRight Petfood"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",6],"just right",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":659
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-N5X2RWL","nickname","Site - Beyond"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"beyond",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":660
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-K499FT9","nickname","Site - Bella"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"bella",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":661
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-WXF7229","nickname","Site - Beneful"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"beneful",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":662
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-54HTSP3","nickname","Site - Mighty Dog"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"mighty-dog",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":663
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-PWCZWZL","nickname","Site - Alpo"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"alpo",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":664
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-MPT89HN","nickname","Site - Waggin Train"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"waggin-train",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"]],
      "tag_id":665
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-KZ5ZBVZ","nickname","Site - Beggin"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"beggin",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":666
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-K2FVF4R","nickname","Site - Tidy Cats"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"tidy-cats",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":667
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-M9DMMXF","nickname","Site - Yesterdays News"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"yesterdays-news",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":668
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-K8QQNCG","nickname","Site - Fancy Feast"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",122],"fancy-feast",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":669
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-TQ4LBCD","nickname","Site - Careers"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",6],"careers",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":670
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-T54K2DR","nickname","Site - Purina Pro Club"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",6],"purina pro club",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":true,
      "vtp_whitelistedTypes":["list",["map","typeId","awct"],["map","typeId","flc"],["map","typeId","sp"],["map","typeId","fls"],["map","typeId","gclidw"],["map","typeId","hl"],["map","typeId","sdl"],["map","typeId","fsl"],["map","typeId","cl"],["map","typeId","tl"],["map","typeId","jel"],["map","typeId","ytl"],["map","typeId","lcl"],["map","typeId","evl"],["map","typeId","vis"],["map","typeId","ctv"],["map","typeId","remm"],["map","typeId","smm"],["map","typeId","c"],["map","typeId","d"],["map","typeId","e"],["map","typeId","f"],["map","typeId","j"],["map","typeId","k"],["map","typeId","r"],["map","typeId","u"],["map","typeId","v"],["map","typeId","dbg"],["map","typeId","ev"],["map","typeId","cid"],["map","typeId","aev"],["map","typeId","jsm"],["map","typeId","crto"],["map","typeId","html"],["map","typeId","ljs"],["map","typeId","twitter_website_tag"],["map","typeId","img"],["map","typeId","tg"]],
      "tag_id":671
    },{
      "function":"__zone",
      "once_per_event":true,
      "vtp_childContainers":["list",["map","publicId","GTM-PR9L6H2","nickname","Site - ProPlanVetDirect"]],
      "vtp_boundaries":["list",["zb","_eq",["macro",6],"pro plan vet direct",false,false],["zb","_re",["macro",18],"fname|lname|first_name|last_name|@|firstname|lastname",true,true],["zb","_re",["macro",12],"fname|lname|first_name|last_name|@|firstname|lastname",true,true]],
      "vtp_enableTypeRestrictions":false,
      "tag_id":672
    },{
      "function":"__cl",
      "tag_id":673
    },{
      "function":"__sdl",
      "vtp_verticalThresholdUnits":"PERCENT",
      "vtp_verticalThresholdsPercent":"25,50,75,100",
      "vtp_verticalThresholdOn":true,
      "vtp_triggerStartOption":"WINDOW_LOAD",
      "vtp_horizontalThresholdOn":false,
      "vtp_uniqueTriggerId":"6714519_150",
      "vtp_enableTriggerStartOption":true,
      "tag_id":674
    },{
      "function":"__ytl",
      "vtp_progressThresholdsPercent":"5,25,50,75,100",
      "vtp_captureComplete":true,
      "vtp_captureStart":true,
      "vtp_fixMissingApi":true,
      "vtp_triggerStartOption":"DOM_READY",
      "vtp_radioButtonGroup1":"PERCENTAGE",
      "vtp_capturePause":true,
      "vtp_captureProgress":true,
      "vtp_uniqueTriggerId":"6714519_153",
      "vtp_enableTriggerStartOption":true,
      "tag_id":675
    },{
      "function":"__tg",
      "vtp_triggerIds":["list","6714519_431_58","6714519_431_298"],
      "vtp_uniqueTriggerId":"6714519_431",
      "tag_id":676
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_431_58",
      "tag_id":677
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_431_298",
      "tag_id":679
    },{
      "function":"__tg",
      "vtp_triggerIds":["list","6714519_444_298","6714519_444_58"],
      "vtp_uniqueTriggerId":"6714519_444",
      "tag_id":680
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_444_298",
      "tag_id":681
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_444_58",
      "tag_id":683
    },{
      "function":"__tg",
      "vtp_triggerIds":["list","6714519_473_298","6714519_473_268"],
      "vtp_uniqueTriggerId":"6714519_473",
      "tag_id":684
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_473_298",
      "tag_id":685
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_473_268",
      "tag_id":687
    },{
      "function":"__tg",
      "vtp_triggerIds":["list","6714519_499_58","6714519_499_298"],
      "vtp_uniqueTriggerId":"6714519_499",
      "tag_id":688
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_499_58",
      "tag_id":689
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_499_298",
      "tag_id":691
    },{
      "function":"__lcl",
      "vtp_waitForTags":true,
      "vtp_checkValidation":false,
      "vtp_waitForTagsTimeout":"2000",
      "vtp_uniqueTriggerId":"6714519_526",
      "tag_id":692
    },{
      "function":"__tg",
      "vtp_triggerIds":["list","6714519_647_58","6714519_647_298"],
      "vtp_uniqueTriggerId":"6714519_647",
      "tag_id":693
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_647_58",
      "tag_id":694
    },{
      "function":"__tg",
      "vtp_isListeningTag":true,
      "vtp_firingId":"6714519_647_298",
      "tag_id":696
    },{
      "function":"__lcl",
      "vtp_waitForTags":true,
      "vtp_checkValidation":false,
      "vtp_waitForTagsTimeout":"2000",
      "vtp_uniqueTriggerId":"6714519_681",
      "tag_id":697
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003Ewindow.ACOE=function(){var m=function(a){return(a=document.cookie.match(\"(^|;)\\\\s*\"+a+\"\\\\s*\\x3d\\\\s*([^;]+)\"))?a.pop():\"\"},n=function(a,b,c){var e=new Date;e.setDate(e.getDate()+c);document.cookie=a+\"\\x3d\"+escape(b)+\";path\\x3d\/\"+(null===c?\"\":\";expires\\x3d\"+e.toUTCString())},p=function(a,b){b=b||\"",["escape",["macro",142],7],"\";console.log(b+\" - \"+a)},q=function(a,b){b||(b=window.location.href);a=a.replace(\/[\\[\\]]\/g,\"\\\\$\\x26\");a=new RegExp(\"[?\\x26]\"+a+\"(\\x3d([^\\x26#]*)|\\x26|#|$)\",\"i\");return(b=a.exec(b))?b[2]?\ndecodeURIComponent(b[2].replace(\/\\+\/g,\" \")):\"\":null},r=function(a){var b=document;if(\"iframe\"===a.type){var c=b.createElement(\"iframe\");c.setAttribute(\"height\",\"1\");c.setAttribute(\"width\",\"1\");c.setAttribute(\"style\",\"display:none\");c.setAttribute(\"src\",a.src)}else{if(\"img\"===a.type){c=new Image;c.src=a.src;return}c=b.createElement(\"script\");c.language=\"javascript\";c.type=\"text\/javascript\";c.async=1;c.charset=\"utf-8\";c.src=a.src}a.id\u0026\u0026(c.id=a.id);\"function\"===typeof a.callback\u0026\u0026(c.addEventListener?\nc.addEventListener(\"load\",function(){a.callback()},!1):c.onreadystatechange=function(){if(\"complete\"===this.readyState||\"loaded\"===this.readyState)this.onreadystatechange=null,a.callback()});var e=a.where||\"head\";(b=b.getElementsByTagName(e)[0])\u0026\u0026(\"script\"===e?b.parentNode.insertBefore(c,b):b.appendChild(c))},t=function(a){window.fb_pixels=window.fb_pixels||{};a=a||{};window.fb_pixels.hasOwnProperty(a.id)||(!function(c,e,f,h,d,g,k){c.fbq||(d=c.fbq=function(){d.callMethod?d.callMethod.apply(d,arguments):\nd.queue.push(arguments)},c._fbq||(c._fbq=d),d.push=d,d.loaded=!0,d.version=\"2.0\",d.queue=[],g=e.createElement(f),g.async=!0,g.src=h,k=e.getElementsByTagName(f)[0],k.parentNode.insertBefore(g,k))}(window,document,\"script\",\"https:\/\/connect.facebook.net\/en_US\/fbevents.js\"),fbq(\"init\",a.id),fbq(\"track\",\"PageView\"),window.fb_pixels[a.id]=1);var b=\"trackSingle\";a.tracktype\u0026\u0026(b=a.tracktype);a.action\u0026\u0026\"PageView\"!=a.action\u0026\u0026(\"track\"!=b?a.fbd?fbq(b,a.id,a.action,a.fbd):fbq(b,a.id,a.action):a.fbd?fbq(\"track\",\na.action,a.fbd):fbq(\"track\",a.action))},u=function(a,b,c,e,f,h,d){d=window.google_tag_manager[",["escape",["macro",142],8,16],"].dataLayer.get(\"evidonConsentGiven\");if(\"undefined\"==typeof d||\"none\"===d||1==d)\"object\"!==typeof a\u0026\u0026(a={eventCategory:b,eventAction:c,eventLabel:e,eventValue:f,nonInteraction:h}),sessionStorage\u0026\u0026\"true\"==sessionStorage.getItem(\"purLog\")\u0026\u0026console.table(a),a.event=\"trackEvent\",a.metrics||(a.metrics=void 0),a.dimensions||(a.dimensions=void 0),a.eventValue||(a.eventValue=void 0),a.nonInteraction||\n(a.nonInteraction=0),a.eventCallback||(a.eventCallback=void 0),purData.push({metrics:void 0,dimensions:void 0}),purData.push(a),a.socialNetwork\u0026\u0026(a.event=\"trackSocial\",purData.push(JSON.parse(JSON.stringify(a)))),",["escape",["macro",143],8,16],"\u0026\u0026\"undefined\"!==typeof ACOE.vendors.bluekai\u0026\u0026\"scroll depth\"!==a.eventCategory\u0026\u0026ACOE.vendors.bluekai.doTag([[\"category\",a.eventCategory],[\"action\",a.eventAction],[\"label\",a.eventLabel]]),",["escape",["macro",144],8,16],"\u0026\u0026\"undefined\"!==typeof jstag\u0026\u0026\"object\"==typeof jstag\u0026\u0026\"function\"==\ntypeof jstag.send\u0026\u0026(a=JSON.parse(JSON.stringify(a)),delete a.event,delete a.dimensions,delete a.metrics,delete a.nonInteraction,delete a[\"gtm.uniqueEventId\"],jstag.send(a))},l=function(a){var b=window.google_tag_manager[",["escape",["macro",142],8,16],"].dataLayer.get(\"evidonConsentGiven\");if(\"undefined\"==typeof b||\"none\"===b||!0===b){a=\"string\"==typeof a?{page:a}:a||{};if(b=a.page){\"undefined\"!==typeof b\u0026\u0026b.match(\/\\\/virtual\/i)||(b=b.split(\"?\"),b=(b[0]+\"\/virtualpageview\").replace(\"\/\/virtual\",\"\/virtual\")+(b[1]?\n\"?\"+b[1]:\"\"));",["escape",["macro",143],8,16],"\u0026\u0026\"function\"==typeof bk_doJSTag\u0026\u0026ACOE.vendors.bluekai.doTag([[\"event\",\"ga_virtualPageView\"],[\"pageName\",b]]);if(",["escape",["macro",144],8,16],"\u0026\u0026\"undefined\"!==typeof jstag\u0026\u0026\"object\"==typeof jstag\u0026\u0026\"function\"==typeof jstag.send){var c=JSON.parse(JSON.stringify(a));c.ga_virtualPageView=b;delete c.page;delete c.dimensions;delete c.metrics;jstag.send(c)}a.page=b}a.event=\"trackPV\";purData.push(JSON.parse(JSON.stringify(a)));a.event=\"trackPVNestleGlobal\";purData.push(JSON.parse(JSON.stringify(a)))}};\nl();window.purinaTrackEvent=u;window.purinaTrackPageview=l;purData.push({event:\"trackLytics\"});return{utils:{getCookie:m,setCookie:n,log:p,getQueryParam:q},tags:{loader:r,facebookLoader:t},vendors:{}}}();purData.push({event:\"ACOE.loaded\",acoe_loaded:!0});\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":7
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":"\u003Cscript type=\"text\/gtmscript\"\u003Edocument.querySelector(\"body\").addEventListener(\"mousedown\",function(a){a=a.target;var c=a.parentElement,d=c.parentElement,b=function(a){return a.getAttribute(\"data-category\")\u0026\u0026a.getAttribute(\"data-action\")?a:void 0};(a=b(a)||b(c)||b(d))\u0026\u0026purinaTrackEvent({eventCategory:a.getAttribute(\"data-category\"),eventAction:a.getAttribute(\"data-action\"),eventLabel:a.getAttribute(\"data-label\"),eventId:a.getAttribute(\"data-event-id\"),eventDesc:a.getAttribute(\"data-event-description\")})});\u003C\/script\u003E",
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":10
    },{
      "function":"__html",
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003EpurinaTrackPageview(",["escape",["macro",146],8,16],");\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":11
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003E",["escape",["macro",143],8,16],"\u0026\u0026(ACOE.vendors.bluekai={},ACOE.vendors.bluekai.doTag=function(a,b){if(\"undefined\"==typeof bk_addPageCtx)ACOE.vendors.bluekai.queue?ACOE.vendors.bluekai.queue.push(a):ACOE.vendors.bluekai.queue=[a];else{window.bk_use_multiple_iframes=!0;window.bk_allow_multiple_calls=!0;bk_addPageCtx(\"tms\",\"gtm\");\"undefined\"!==typeof a\u0026\u00260\u003Ca.length\u0026\u0026a.forEach(function(a){bk_addPageCtx(a[0],a[1])});ACOE.utils.getCookie(\"bk\")\u0026\u0026bk_addPageCtx(\"id\",ACOE.utils.getCookie(\"bk\"));if(\"purina.com\"==",["escape",["macro",7],8,16],")try{",["escape",["macro",120],8,16],"\u0026\u0026\n\"(not set)\"!==",["escape",["macro",120],8,16],"\u0026\u0026bk_addPageCtx(\"brandID\",",["escape",["macro",120],8,16],"),",["escape",["macro",91],8,16],"\u0026\u0026\"(not set)\"!==",["escape",["macro",91],8,16],"\u0026\u0026bk_addPageCtx(\"page_pet_type\",",["escape",["macro",91],8,16],"),",["escape",["macro",87],8,16],"\u0026\u0026\"(not set)\"!==",["escape",["macro",87],8,16],"\u0026\u0026bk_addPageCtx(\"page_brand\",",["escape",["macro",87],8,16],"),",["escape",["macro",85],8,16],"\u0026\u0026\"(not set)\"!==",["escape",["macro",85],8,16],"\u0026\u0026bk_addPageCtx(\"content_type\",",["escape",["macro",85],8,16],"),",["escape",["macro",89],8,16],"\u0026\u0026\"(not set)\"!==",["escape",["macro",89],8,16],"\u0026\u0026bk_addPageCtx(\"page_pet_age\",\n",["escape",["macro",89],8,16],"),\"undefined\"!==typeof lio\u0026\u0026(\"undefined\"!==typeof lio._uid\u0026\u0026bk_addPageCtx(\"lioID\",lio._uid),\"undefined\"!==typeof lio.segmentsArray\u0026\u0026bk_addPageCtx(\"lio_segments\",lio.segmentsArray.toString()))}catch(c){}\"function\"==typeof ACOE_BlueKaiLoader\u0026\u0026b\u0026\u0026ACOE_BlueKaiLoader();BKTAG.doTag(",["escape",["macro",143],8,16],",10,!1,null,!0)}},ACOE.tags.loader({type:\"script\",src:\"\/\/tags.bkrtx.com\/js\/bk-coretag.js\",callback:function(){ACOE.vendors.bluekai.doTag(void 0,!0);var a=ACOE.vendors.bluekai.queue;\n\"object\"==typeof a\u0026\u00260\u003Ca.length\u0026\u0026(a.forEach(function(a){ACOE.vendors.bluekai.doTag(a)}),ACOE.vendors.bluekai.queue=null)}}));\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":16
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003E(function(){var a=!0;\/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini\/i.test(navigator.userAgent);a\u0026\u0026ACOE.tags.loader({type:\"script\",src:\"",["escape",["macro",148],7],"\"})})();\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":18
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_load":true,
      "vtp_html":"\u003Cscript type=\"text\/gtmscript\"\u003E(function(){var e=function(b,a,c){purinaTrackEvent({eventCategory:\"social\",eventAction:b,eventLabel:a,socialNetwork:a,socialAction:b,socialTarget:c})};if(window.FB)for(var d=[{\"edge.create\":\"like\"},{\"edge.remove\":\"unlike\"},{\"message.send\":\"send\"},{\"message.comment\":\"comment\"}],a=0;a\u003Cd.length;a++)FB.Event.subscribe(Object.keys(d[a])[0],function(b){e(d[a][Object.keys(d[a])],\"facebook\",b);ACOE.utils.log(\"social event: fb\")});ACOE.tags.loader({type:\"script\",src:\"\/\/platform.twitter.com\/widgets.js\",id:\"twitter-wjs\",\ncallback:function(){twttr.ready(function(a){for(var b=[\"click\",\"tweet\",\"retweet\",\"like\",\"follow\"],c=0;c\u003Cb.length;c++)a.events.bind(b[c],function(a){e(a.type,\"twitter\",location.href);ACOE.utils.log(\"social event: twitter\")})})}})})();\u003C\/script\u003E",
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":28
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003Evar pCat=(",["escape",["macro",102],8,16],"||\"\").toLowerCase(),pAct=(",["escape",["macro",103],8,16],"||\"\").toLowerCase(),pLab=(",["escape",["macro",104],8,16],"||\"\").toLowerCase();\nif(\"support\"===pCat\u0026\u0026\"successful submission\"===pLab||\"contact us form\"===pCat\u0026\u0026\"submit\"===pAct)purData.push({event:\"trackEventNestle\",eventCategory:\"Contact Us form\",eventAction:\"Submit\",eventLabel:document.location.href});else if(\"bv ratings and reviews\"===pCat||\"product-details page\"===pCat\u0026\u0026\"write review\"===pAct){var nAct=pAct.match(\/write review\/i)?\"BV Write Review\":\"\";if(!nAct)switch(pAct){case \"bv overall rating\":nAct=\"BV Overall Rating\";break;case \"bv review body\":nAct=\"BV Review Body\";break;\ncase \"bv submit\":nAct=\"BV Post Review\"}nAct\u0026\u0026purData.push({event:\"trackEventNestle\",eventCategory:\"BV ratings and reviews\",eventAction:nAct,eventLabel:document.location.href})};\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":35
    },{
      "function":"__html",
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003EpurinaTrackEvent({eventCategory:\"scroll depth\",eventAction:\"",["escape",["macro",20],7],"\",eventLabel:\"",["escape",["macro",150],7],"% viewed\",nonInteraction:1});\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":40
    },{
      "function":"__html",
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003EpurinaTrackEvent({eventCategory:\"video\",eventAction:",["escape",["macro",153],8,16],",eventLabel:",["escape",["macro",157],8,16],"});\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":41
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003EACOE.tags.loader({type:\"script\",src:\"",["escape",["macro",158],7],"\"});\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":49
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":"\u003Cscript type=\"text\/gtmscript\"\u003EACOE.tags.loader({type:\"script\",src:\"\/\/d2oh4tlt9mrke9.cloudfront.net\/Record\/js\/sessioncam.recorder.js\",callback:function(){purData.push({event:\"sessionCamLoaded\"})}});\u003C\/script\u003E",
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":52
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":["template","\u003Cscript type=\"text\/gtmscript\"\u003Evar lioInit={cid:\"",["escape",["macro",161],7],"\",url:\"\/\/c.lytics.io\",min:!0,loadid:!0,stream:\"",["escape",["macro",5],7],"\".replace(\/ \/gi,\"_\")};\nwindow.jstag=function(){function d(a){return function(){return a.apply(this,arguments),this}}function c(){var a=[\"ready\"].concat(e.call(arguments));return d(function(){a.push(e.call(arguments));this._q.push(a)})}var a={_q:[],_c:{},ts:(new Date).getTime(),ver:\"2.0.0\"},e=Array.prototype.slice;return a.init=function(b){return a._c=b,b.synchronous||a.loadtagmgr(b),this},a.loadtagmgr=function(a){var b=document.createElement(\"script\");b.type=\"text\/javascript\";b.async=!0;b.src=a.url+\"\/api\/tag\/\"+a.cid+\"\/lio.js\";\na=document.getElementsByTagName(\"script\")[0];a.parentNode.insertBefore(b,a)},a.ready=c(),a.send=c(\"send\"),a.mock=c(\"mock\"),a.identify=c(\"identify\"),a.pageView=c(\"pageView\"),a.bind=d(function(b){a._q.push([b,e.call(arguments,1)])}),a.block=d(function(){a._c.blockload=!0}),a.unblock=d(function(){a._c.blockload=!1}),a}();window.jstag.init(lioInit);\nvar dimensions={ansira_id:",["escape",["macro",78],8,16],",brand_id:",["escape",["macro",162],8,16],",content_type:",["escape",["macro",85],8,16],",pageBrand:",["escape",["macro",87],8,16],",pagePetType:",["escape",["macro",91],8,16],",pagePetAge:",["escape",["macro",89],8,16],",pageType:",["escape",["macro",93],8,16],",pageProductFunctionalHealth:",["escape",["macro",95],8,16],",pageProductType:",["escape",["macro",97],8,16],",userCity:",["escape",["macro",163],8,16],",userState:",["escape",["macro",164],8,16],",userZip:",["escape",["macro",165],8,16],",userCountry:",["escape",["macro",166],8,16],",userPetOwnership:",["escape",["macro",167],8,16],",\nuserPetType:",["escape",["macro",168],8,16],",userPetAge:",["escape",["macro",169],8,16],",userPetSize:",["escape",["macro",170],8,16],",userPetGender:",["escape",["macro",171],8,16],",userPetBreed:",["escape",["macro",172],8,16],",userPetNumber:",["escape",["macro",173],8,16],",userPetDietaryNeeds:",["escape",["macro",174],8,16],",userPetName:",["escape",["macro",175],8,16],",userPetSecondaryBreed:",["escape",["macro",176],8,16],",userPetShelterName:",["escape",["macro",177],8,16],",userPetShelterID:",["escape",["macro",178],8,16],",userPetAcquisitionType:",["escape",["macro",179],8,16],",userPetBirthMonth:",["escape",["macro",180],8,16],",\npetProfilePetID:",["escape",["macro",181],8,16],",petProfilePetName:",["escape",["macro",182],8,16],",petProfileAnimalType:",["escape",["macro",183],8,16],",petProfileSpecies:",["escape",["macro",184],8,16],",petProfileAge:",["escape",["macro",185],8,16],",petProfileGender:",["escape",["macro",186],8,16],",petProfileSize:",["escape",["macro",187],8,16],",petProfilePrimaryBreed:",["escape",["macro",188],8,16],",petProfileSecondaryBreed:",["escape",["macro",189],8,16],",petProfileMixedBreed:",["escape",["macro",190],8,16],",petProfilePrimaryColor:",["escape",["macro",191],8,16],",petProfileCoatLength:",["escape",["macro",192],8,16],",\npetProfilePetCharacteristics:",["escape",["macro",193],8,16],",petProfileGoodWith:",["escape",["macro",194],8,16],",petProfilePetZipCode:",["escape",["macro",195],8,16],",petProfileShelterID:",["escape",["macro",196],8,16],",petProfileShelterName:",["escape",["macro",197],8,16],",petProfileArrivalDate:",["escape",["macro",198],8,16],",petProfilePhotosInProfile:",["escape",["macro",199],8,16],",petProfileVideoPresent:",["escape",["macro",200],8,16],",petProfileAdoptionFee:",["escape",["macro",201],8,16],",petProfilePetStatus:",["escape",["macro",202],8,16],"},key;\nfor(key in dimensions){jstag.send(dimensions);break};\u003C\/script\u003E"],
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":54
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":"\u003Cscript type=\"text\/gtmscript\"\u003Ewindow.dataLayer=window.dataLayer||[];\n(function(b){try{if(Array.isArray(b)){var c=b.push,d=function(){if(\"BuyNowEvent\"===arguments[0].event\u0026\u0026\"PriceSpider BuyNow product\"===arguments[0].category){var a=arguments[0].label.split(\" | \");purinaTrackEvent({event:\"trackEvent\",eventCategory:arguments[0].category.toLowerCase(),eventAction:arguments[0].action.toLowerCase(),eventLabel:(a[0]+\" | \"+a[4]+\" | \"+a[5]+\" | \"+a[6]).toLowerCase(),nonInteraction:\"BuyNow open\"===arguments[0].action?1:0,dimensions:{19:a[4].toLowerCase()}});purData.push({event:\"trackEventNestle\",\neventCategory:arguments[0].category,eventAction:arguments[0].action,eventLabel:arguments[0].label})}c.apply(this,arguments)};b.push=d}}catch(a){console.log(a)}})(window.dataLayer);\u003C\/script\u003E",
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":64
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_load":true,
      "vtp_html":"\u003Cscript type=\"text\/gtmscript\"\u003E(function(f){function a(d,k,e){var b=document,c=\"script\",a=b.getElementsByTagName(c)[0];a||(a=b.head);b=b.createElement(c);b.async=e;b.id=d;b.src=k;b.charset=\"utf-8\";a.parentNode.insertBefore(b,a)}function l(){var d=window.location.hostname.split(\".\");if(2===d.length)c=d[0];else if(2\u003Cd.length){var a=d[d.length-2];var e=a;var b=\"co com info web info gov edu biz net org\".split(\" \"),f=\"uk us fr es de at au ae be br ca ch cn co cz dk eg eu fi gb gr hk hr hu ie in jp mx nl no nz pl ro ru se\".split(\" \");\nc=(e=-1!==b.indexOf(e)||-1!==f.indexOf(e))?d[d.length-3]:a}return c}window.evidon={};window.evidon.id=f;window.evidon.test=!1;var h=\"\/\/c.evidon.com\/\",c=l(),g=h+\"sitenotice\/\";a(\"evidon-notice\",g+\"evidon-sitenotice-tag.js\",!1);a(\"evidon-location\",h+\"geo\/country.js\",!0);a(\"evidon-themes\",g+f+\"\/snthemes.js\",!0);c\u0026\u0026a(\"evidon-settings\",g+f+\"\/\"+c+(window.evidon.test?\"\/test\":\"\")+\"\/settings.js\",!0);window.evidon.priorConsentCallback=function(a,c,e){purData.push({event:\"evidonConsentGiven\",evidonConsentGiven:!0,\ncategories:a,vendors:c,cookies:e})};window.evidon.closeCallback=function(){purData.push({evidonConsentGiven:!1})};window.evidon.consentWithdrawnCallback=function(){purData.push({evidonConsentGiven:!1})};window.evidon.consentDeclinedCallback=function(){purData.push({evidonConsentGiven:!1})}})(2020);\u003C\/script\u003E",
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":68
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":"\u003Cscript type=\"text\/gtmscript\"\u003EACOE.tags.loader({type:\"script\",src:\"\/\/cdn.pricespider.com\/1\/2958\/ps-utid.js\"});\u003C\/script\u003E",
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":70
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":"\u003Cscript type=\"text\/gtmscript\"\u003Ewindow.jstag=function(){function d(a){return function(){return a.apply(this,arguments),this}}function c(){var a=[\"ready\"].concat(e.call(arguments));return d(function(){a.push(e.call(arguments));this._q.push(a)})}var a={_q:[],_c:{},ts:(new Date).getTime(),ver:\"2.0.0\"},e=Array.prototype.slice;return a.init=function(b){return a._c=b,b.synchronous||a.loadtagmgr(b),this},a.loadtagmgr=function(a){var b=document.createElement(\"script\");b.type=\"text\/javascript\";b.async=!0;b.src=a.url+\"\/api\/tag\/\"+a.cid+\"\/lio.js\";\na=document.getElementsByTagName(\"script\")[0];a.parentNode.insertBefore(b,a)},a.ready=c(),a.send=c(\"send\"),a.mock=c(\"mock\"),a.identify=c(\"identify\"),a.pageView=c(\"pageView\"),a.bind=d(function(b){a._q.push([b,e.call(arguments,1)])}),a.block=d(function(){a._c.blockload=!0}),a.unblock=d(function(){a._c.blockload=!1}),a}();window.jstag.init({cid:\"9ae562c78c038c6b98bf80cfbe5a859a\",url:\"\/\/c.lytics.io\",min:!0,loadid:!1});\u003C\/script\u003E",
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":504
    },{
      "function":"__html",
      "metadata":["map"],
      "once_per_event":true,
      "vtp_html":"\u003Cscript type=\"text\/gtmscript\"\u003E!function(d,a){a.liosetup=a.liosetup||{};a.liosetup.callback=a.liosetup.callback||[];a.liosetup.addEntityLoadedCallback=function(b,e){if(\"function\"==typeof a.liosetup.callback){var c=[];c.push(a.liosetup.callback);a.liosetup.callback=c}a.lio\u0026\u0026a.lio.loaded?b(a.lio.data):e?a.liosetup.callback.unshift(b):a.liosetup.callback.push(b)}}(document,window);\nwindow.liosetup.addEntityLoadedCallback(function(d){lio instanceof Object\u0026\u0026purinaTrackEvent({eventCategory:\"lytics\",eventAction:\"lytics_google_integration\",dimensions:{20:lio._uid,21:lio.segmentsString},nonInteraction:1})});\u003C\/script\u003E",
      "vtp_supportDocumentWrite":false,
      "vtp_enableIframeMode":false,
      "vtp_enableEditJsMacroBehavior":false,
      "tag_id":646
    }],
  "predicates":[{
      "function":"_cn",
      "arg0":["macro",0],
      "arg1":"nestlepurinacareers.com"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"gtm.triggerGroup"
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_499($|,)))"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"trackPV"
    },{
      "function":"_eq",
      "arg0":["macro",7],
      "arg1":"dev and qa"
    },{
      "function":"_eq",
      "arg0":["macro",7],
      "arg1":"purina pack"
    },{
      "function":"_eq",
      "arg0":["macro",7],
      "arg1":"catch all"
    },{
      "function":"_eq",
      "arg0":["macro",7],
      "arg1":"petfinder"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"trackPVPurinaGlobal"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"trackEvent"
    },{
      "function":"_cn",
      "arg0":["macro",106],
      "arg1":"undefined"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"trackPVNestleGlobal"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"trackEventNestle"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"trackSocial"
    },{
      "function":"_cn",
      "arg0":["macro",122],
      "arg1":"undefined"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"trackEventSocial"
    },{
      "function":"_eq",
      "arg0":["macro",5],
      "arg1":"purina institute"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"gtm.js"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"evidonConsentGiven"
    },{
      "function":"_eq",
      "arg0":["macro",128],
      "arg1":"(not set)"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"gtm.dom"
    },{
      "function":"_cn",
      "arg0":["macro",11],
      "arg1":"virtualpageview"
    },{
      "function":"_re",
      "arg0":["macro",129],
      "arg1":"fname|lname|first_name|last_name|@|firstname|lastname|\\sfile\\s\\\"",
      "ignore_case":true
    },{
      "function":"_re",
      "arg0":["macro",1],
      "arg1":".+"
    },{
      "function":"_re",
      "arg0":["macro",103],
      "arg1":"buy online|buy\\-online"
    },{
      "function":"_eq",
      "arg0":["macro",102],
      "arg1":"signup"
    },{
      "function":"_eq",
      "arg0":["macro",104],
      "arg1":"successful submission"
    },{
      "function":"_cn",
      "arg0":["macro",103],
      "arg1":"coupon"
    },{
      "function":"_cn",
      "arg0":["macro",103],
      "arg1":"email"
    },{
      "function":"_re",
      "arg0":["macro",104],
      "arg1":"successful submission"
    },{
      "function":"_eq",
      "arg0":["macro",103],
      "arg1":"WIDGET DEFAULT TEMPLATE"
    },{
      "function":"_re",
      "arg0":["macro",104],
      "arg1":"successful submission",
      "ignore_case":true
    },{
      "function":"_eq",
      "arg0":["macro",102],
      "arg1":"support"
    },{
      "function":"_eq",
      "arg0":["macro",104],
      "arg1":"crm-yes"
    },{
      "function":"_cn",
      "arg0":["macro",103],
      "arg1":"contact us"
    },{
      "function":"_eq",
      "arg0":["macro",134],
      "arg1":"true"
    },{
      "function":"_re",
      "arg0":["macro",136],
      "arg1":"^javascript|mailto",
      "ignore_case":true
    },{
      "function":"_re",
      "arg0":["macro",133],
      "arg1":"profiles\\.(purina|petfinder)\\.com",
      "ignore_case":true
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"gtm.linkClick"
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_681($|,)))"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"purina institute"
    },{
      "function":"_re",
      "arg0":["macro",138],
      "arg1":"zip|mp\\\\d+|mpe*g|pdf|docx*|pptx*|xlsx*|jpe*g|png|gif|tiff*",
      "ignore_case":true
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_526($|,)))"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"mypup"
    },{
      "function":"_cn",
      "arg0":["macro",0],
      "arg1":"mypupapp.uspurina.acsitefactory.com"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"gtm.load"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"ACOE.loaded"
    },{
      "function":"_eq",
      "arg0":["macro",5],
      "arg1":"purina.com"
    },{
      "function":"_re",
      "arg0":["macro",18],
      "arg1":".+",
      "ignore_case":true
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_431($|,)))"
    },{
      "function":"_re",
      "arg0":["macro",146],
      "arg1":".+"
    },{
      "function":"_eq",
      "arg0":["macro",147],
      "arg1":"true"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"gtm.click"
    },{
      "function":"_eq",
      "arg0":["macro",143],
      "arg1":"undefined"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"just right"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"growing pup"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"purina pro club"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"petfinder"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"pro plan vet direct"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"p4p"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"purina shelter champions"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"purina store"
    },{
      "function":"_re",
      "arg0":["macro",0],
      "arg1":"dev\\.tesla\\.purina\\.com|test\\.tesla\\.purina\\.com",
      "ignore_case":true
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"petqcheck"
    },{
      "function":"_eq",
      "arg0":["macro",7],
      "arg1":"pet support alliance"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"reduce cat allergens"
    },{
      "function":"_cn",
      "arg0":["macro",6],
      "arg1":"purina.com"
    },{
      "function":"_re",
      "arg0":["macro",149],
      "arg1":"bv ratings and reviews|contact us form|product-details page|write review|^support",
      "ignore_case":true
    },{
      "function":"_re",
      "arg0":["macro",7],
      "arg1":"dev and qa|catch all|purina.com"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"gtm.scrollDepth"
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_150($|,)))"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"gtm.video"
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_153($|,)))"
    },{
      "function":"_re",
      "arg0":["macro",0],
      "arg1":"(int|preprod)\\.justrightpetfood\\.com",
      "ignore_case":true
    },{
      "function":"_re",
      "arg0":["macro",1],
      "arg1":".*"
    },{
      "function":"_cn",
      "arg0":["macro",7],
      "arg1":"tidy cats"
    },{
      "function":"_re",
      "arg0":["macro",0],
      "arg1":"(www|pro)\\-qa\\.petfinder\\.com"
    },{
      "function":"_re",
      "arg0":["macro",144],
      "arg1":".+"
    },{
      "function":"_eq",
      "arg0":["macro",144],
      "arg1":"undefined"
    },{
      "function":"_eq",
      "arg0":["macro",1],
      "arg1":"trackLytics"
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_473($|,)))"
    },{
      "function":"_eq",
      "arg0":["macro",6],
      "arg1":"purina.com"
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_444($|,)))"
    },{
      "function":"_eq",
      "arg0":["macro",7],
      "arg1":"careers"
    },{
      "function":"_eq",
      "arg0":["macro",144],
      "arg1":"1"
    },{
      "function":"_re",
      "arg0":["macro",2],
      "arg1":"(^$|((^|,)6714519_647($|,)))"
    }],
  "rules":[
    [["if",1,2],["unless",0],["add",0]],
    [["if",3],["add",1]],
    [["if",8],["unless",4,5,6,7],["add",2]],
    [["if",9],["unless",4,5,6,7],["add",3]],
    [["if",9],["add",4]],
    [["if",11],["unless",5,6,10],["add",5]],
    [["if",12],["add",6]],
    [["if",13],["add",7]],
    [["if",13],["unless",4,5,6,7],["add",8]],
    [["if",3],["unless",4,14],["add",9]],
    [["if",15],["unless",4,14],["add",10]],
    [["if",9],["unless",4,14],["add",11]],
    [["if",17],["unless",16],["add",12,67]],
    [["if",18],["add",12,67]],
    [["if",20],["unless",19],["add",13,14]],
    [["if",3,21],["add",13,14]],
    [["if",9,24],["unless",19],["add",15]],
    [["if",9,25,26,27],["unless",19],["add",16,17]],
    [["if",9,25,28,29],["unless",19],["add",17]],
    [["if",9,25,30,31],["unless",19],["add",17]],
    [["if",9,32,33,34],["unless",19],["add",17]],
    [["if",35,38,39],["unless",36,37],["add",18]],
    [["if",38,41,42],["add",19]],
    [["if",17,43],["add",20]],
    [["if",17,44],["add",20]],
    [["if",17],["add",21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,56,59,63]],
    [["if",45],["add",48]],
    [["if",20],["add",49,51,55,60,64]],
    [["if",46],["add",52,54,57,61,65]],
    [["if",45,47],["add",58,77]],
    [["if",17,48],["add",62,66]],
    [["if",1,49],["add",68,71,72,76]],
    [["if",50,51,52],["add",69]],
    [["if",46],["unless",53],["add",70]],
    [["if",9,67],["add",73]],
    [["if",51,69,70],["unless",68],["add",74]],
    [["if",51,71,72],["add",75]],
    [["if",45,75],["add",77]],
    [["if",45,76],["add",77]],
    [["if",7,45],["add",77]],
    [["if",45,54],["add",77]],
    [["if",45,61],["add",77]],
    [["if",77,79],["unless",78],["add",78]],
    [["if",1,80],["add",79]],
    [["if",16,17],["add",80]],
    [["if",1,81,82],["add",81]],
    [["if",46,83],["add",82]],
    [["if",1,84,85],["add",83]],
    [["if",22,23],["block",13,14,15,16,17,70]],
    [["if",23,40],["block",18,19,71,76]],
    [["if",23,54],["block",71]],
    [["if",23,55],["block",71,72,76]],
    [["if",23,56],["block",71,76]],
    [["if",23,57],["block",71]],
    [["if",23,58],["block",71,76]],
    [["if",23,59],["block",71,76]],
    [["if",23,60],["block",71,76]],
    [["if",23,61],["block",71]],
    [["if",23,62],["block",71]],
    [["if",23,63],["block",71,76]],
    [["if",23,64],["block",71,76]],
    [["if",23,65],["block",71,76]],
    [["if",23,66],["block",72]],
    [["if",73,74],["block",76]]]
},
"runtime":[]




};
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var aa,ba="function"==typeof Object.create?Object.create:function(a){var b=function(){};b.prototype=a;return new b},da;if("function"==typeof Object.setPrototypeOf)da=Object.setPrototypeOf;else{var ea;a:{var fa={Nf:!0},ha={};try{ha.__proto__=fa;ea=ha.Nf;break a}catch(a){}ea=!1}da=ea?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}
var ia=da,ja=function(a,b){a.prototype=ba(b.prototype);a.prototype.constructor=a;if(ia)ia(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c]},ka=this||self,ma=/^[\w+/_-]+[=]{0,2}$/,oa=null;var pa=function(){},qa=function(a){return"function"==typeof a},g=function(a){return"string"==typeof a},ra=function(a){return"number"==typeof a&&!isNaN(a)},sa=function(a){return"[object Array]"==Object.prototype.toString.call(Object(a))},ta=function(a,b){if(Array.prototype.indexOf){var c=a.indexOf(b);return"number"==typeof c?c:-1}for(var d=0;d<a.length;d++)if(a[d]===b)return d;return-1},ua=function(a,b){if(a&&sa(a))for(var c=0;c<a.length;c++)if(a[c]&&b(a[c]))return a[c]},va=function(a,b){if(!ra(a)||
!ra(b)||a>b)a=0,b=2147483647;return Math.floor(Math.random()*(b-a+1)+a)},ya=function(a,b){for(var c=new wa,d=0;d<a.length;d++)c.set(a[d],!0);for(var e=0;e<b.length;e++)if(c.get(b[e]))return!0;return!1},Aa=function(a,b){for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&&b(c,a[c])},Ca=function(a){return Math.round(Number(a))||0},Da=function(a){return"false"==String(a).toLowerCase()?!1:!!a},Ea=function(a){var b=[];if(sa(a))for(var c=0;c<a.length;c++)b.push(String(a[c]));return b},Fa=function(a){return a?
a.replace(/^\s+|\s+$/g,""):""},Ga=function(){return(new Date).getTime()},wa=function(){this.prefix="gtm.";this.values={}};wa.prototype.set=function(a,b){this.values[this.prefix+a]=b};wa.prototype.get=function(a){return this.values[this.prefix+a]};
var Ha=function(a,b,c){return a&&a.hasOwnProperty(b)?a[b]:c},Ia=function(a){var b=!1;return function(){if(!b)try{a()}catch(c){}b=!0}},Ja=function(a,b){for(var c in b)b.hasOwnProperty(c)&&(a[c]=b[c])},Ka=function(a){for(var b in a)if(a.hasOwnProperty(b))return!0;return!1},La=function(a,b){for(var c=[],d=0;d<a.length;d++)c.push(a[d]),c.push.apply(c,b[a[d]]||[]);return c},Ma=function(a,b){for(var c={},d=c,e=a.split("."),f=0;f<e.length-1;f++)d=d[e[f]]={};d[e[e.length-1]]=b;return c},Na=function(a){var b=
[];Aa(a,function(c,d){10>c.length&&d&&b.push(c)});return b.join(",")};/*
 jQuery v1.9.1 (c) 2005, 2012 jQuery Foundation, Inc. jquery.org/license. */
var Oa=/\[object (Boolean|Number|String|Function|Array|Date|RegExp)\]/,Pa=function(a){if(null==a)return String(a);var b=Oa.exec(Object.prototype.toString.call(Object(a)));return b?b[1].toLowerCase():"object"},Qa=function(a,b){return Object.prototype.hasOwnProperty.call(Object(a),b)},Ra=function(a){if(!a||"object"!=Pa(a)||a.nodeType||a==a.window)return!1;try{if(a.constructor&&!Qa(a,"constructor")&&!Qa(a.constructor.prototype,"isPrototypeOf"))return!1}catch(c){return!1}for(var b in a);return void 0===
b||Qa(a,b)},n=function(a,b){var c=b||("array"==Pa(a)?[]:{}),d;for(d in a)if(Qa(a,d)){var e=a[d];"array"==Pa(e)?("array"!=Pa(c[d])&&(c[d]=[]),c[d]=n(e,c[d])):Ra(e)?(Ra(c[d])||(c[d]={}),c[d]=n(e,c[d])):c[d]=e}return c};
var Sa=[],Ta={"\x00":"&#0;",'"':"&quot;","&":"&amp;","'":"&#39;","<":"&lt;",">":"&gt;","\t":"&#9;","\n":"&#10;","\x0B":"&#11;","\f":"&#12;","\r":"&#13;"," ":"&#32;","-":"&#45;","/":"&#47;","=":"&#61;","`":"&#96;","\u0085":"&#133;","\u00a0":"&#160;","\u2028":"&#8232;","\u2029":"&#8233;"},Ua=function(a){return Ta[a]},Wa=/[\x00\x22\x26\x27\x3c\x3e]/g;var $a=/[\x00\x08-\x0d\x22\x26\x27\/\x3c-\x3e\\\x85\u2028\u2029]/g,ab={"\x00":"\\x00","\b":"\\x08","\t":"\\t","\n":"\\n","\x0B":"\\x0b",
"\f":"\\f","\r":"\\r",'"':"\\x22","&":"\\x26","'":"\\x27","/":"\\/","<":"\\x3c","=":"\\x3d",">":"\\x3e","\\":"\\\\","\u0085":"\\x85","\u2028":"\\u2028","\u2029":"\\u2029",$:"\\x24","(":"\\x28",")":"\\x29","*":"\\x2a","+":"\\x2b",",":"\\x2c","-":"\\x2d",".":"\\x2e",":":"\\x3a","?":"\\x3f","[":"\\x5b","]":"\\x5d","^":"\\x5e","{":"\\x7b","|":"\\x7c","}":"\\x7d"},bb=function(a){return ab[a]};Sa[7]=function(a){return String(a).replace($a,bb)};
Sa[8]=function(a){if(null==a)return" null ";switch(typeof a){case "boolean":case "number":return" "+a+" ";default:return"'"+String(String(a)).replace($a,bb)+"'"}};var mb=/[\x00- \x22\x27-\x29\x3c\x3e\\\x7b\x7d\x7f\x85\xa0\u2028\u2029\uff01\uff03\uff04\uff06-\uff0c\uff0f\uff1a\uff1b\uff1d\uff1f\uff20\uff3b\uff3d]/g,ob={"\x00":"%00","\u0001":"%01","\u0002":"%02","\u0003":"%03","\u0004":"%04","\u0005":"%05","\u0006":"%06","\u0007":"%07","\b":"%08","\t":"%09","\n":"%0A","\x0B":"%0B","\f":"%0C","\r":"%0D","\u000e":"%0E","\u000f":"%0F","\u0010":"%10",
"\u0011":"%11","\u0012":"%12","\u0013":"%13","\u0014":"%14","\u0015":"%15","\u0016":"%16","\u0017":"%17","\u0018":"%18","\u0019":"%19","\u001a":"%1A","\u001b":"%1B","\u001c":"%1C","\u001d":"%1D","\u001e":"%1E","\u001f":"%1F"," ":"%20",'"':"%22","'":"%27","(":"%28",")":"%29","<":"%3C",">":"%3E","\\":"%5C","{":"%7B","}":"%7D","\u007f":"%7F","\u0085":"%C2%85","\u00a0":"%C2%A0","\u2028":"%E2%80%A8","\u2029":"%E2%80%A9","\uff01":"%EF%BC%81","\uff03":"%EF%BC%83","\uff04":"%EF%BC%84","\uff06":"%EF%BC%86",
"\uff07":"%EF%BC%87","\uff08":"%EF%BC%88","\uff09":"%EF%BC%89","\uff0a":"%EF%BC%8A","\uff0b":"%EF%BC%8B","\uff0c":"%EF%BC%8C","\uff0f":"%EF%BC%8F","\uff1a":"%EF%BC%9A","\uff1b":"%EF%BC%9B","\uff1d":"%EF%BC%9D","\uff1f":"%EF%BC%9F","\uff20":"%EF%BC%A0","\uff3b":"%EF%BC%BB","\uff3d":"%EF%BC%BD"},pb=function(a){return ob[a]};Sa[16]=function(a){return a};var rb;
var sb=[],tb=[],ub=[],vb=[],wb=[],xb={},yb,zb,Ab,Bb=function(a,b){var c=a["function"];if(!c)throw Error("Error: No function name given for function call.");var d=xb[c],e={},f;for(f in a)a.hasOwnProperty(f)&&0===f.indexOf("vtp_")&&(e[void 0!==d?f:f.substr(4)]=a[f]);return void 0!==d?d(e):rb(c,e,b)},Eb=function(a,b,c){c=c||[];var d={},e;for(e in a)a.hasOwnProperty(e)&&(d[e]=Cb(a[e],b,c));return d},Fb=function(a){var b=a["function"];if(!b)throw"Error: No function name given for function call.";var c=
xb[b];return c?c.priorityOverride||0:0},Cb=function(a,b,c){if(sa(a)){var d;switch(a[0]){case "function_id":return a[1];case "list":d=[];for(var e=1;e<a.length;e++)d.push(Cb(a[e],b,c));return d;case "macro":var f=a[1];if(c[f])return;var h=sb[f];if(!h||b.$c(h))return;c[f]=!0;try{var k=Eb(h,b,c);k.vtp_gtmEventId=b.id;d=Bb(k,b);Ab&&(d=Ab.lg(d,k))}catch(y){b.He&&b.He(y,Number(f)),d=!1}c[f]=!1;return d;case "map":d={};for(var l=1;l<a.length;l+=2)d[Cb(a[l],b,c)]=Cb(a[l+1],b,c);return d;case "template":d=
[];for(var m=!1,r=1;r<a.length;r++){var q=Cb(a[r],b,c);zb&&(m=m||q===zb.Kb);d.push(q)}return zb&&m?zb.og(d):d.join("");case "escape":d=Cb(a[1],b,c);if(zb&&sa(a[1])&&"macro"===a[1][0]&&zb.Mg(a))return zb.dh(d);d=String(d);for(var u=2;u<a.length;u++)Sa[a[u]]&&(d=Sa[a[u]](d));return d;case "tag":var p=a[1];if(!vb[p])throw Error("Unable to resolve tag reference "+p+".");return d={te:a[2],index:p};case "zb":var t={arg0:a[2],arg1:a[3],ignore_case:a[5]};t["function"]=a[1];var v=Gb(t,b,c),w=!!a[4];return w||
2!==v?w!==(1===v):null;default:throw Error("Attempting to expand unknown Value type: "+a[0]+".");}}return a},Gb=function(a,b,c){try{return yb(Eb(a,b,c))}catch(d){JSON.stringify(a)}return 2};var Hb=function(){var a=function(b){return{toString:function(){return b}}};return{Ed:a("convert_case_to"),Fd:a("convert_false_to"),Gd:a("convert_null_to"),Hd:a("convert_true_to"),Id:a("convert_undefined_to"),Hh:a("debug_mode_metadata"),Ha:a("function"),lf:a("instance_name"),rf:a("live_only"),tf:a("malware_disabled"),uf:a("metadata"),Ih:a("original_vendor_template_id"),yf:a("once_per_event"),Nd:a("once_per_load"),Vd:a("setup_tags"),Xd:a("tag_id"),Yd:a("teardown_tags")}}();var Ib=null,Lb=function(a){function b(q){for(var u=0;u<q.length;u++)d[q[u]]=!0}var c=[],d=[];Ib=Jb(a);for(var e=0;e<tb.length;e++){var f=tb[e],h=Kb(f);if(h){for(var k=f.add||[],l=0;l<k.length;l++)c[k[l]]=!0;b(f.block||[])}else null===h&&b(f.block||[])}for(var m=[],r=0;r<vb.length;r++)c[r]&&!d[r]&&(m[r]=!0);return m},Kb=function(a){for(var b=a["if"]||[],c=0;c<b.length;c++){var d=Ib(b[c]);if(0===d)return!1;if(2===d)return null}for(var e=a.unless||[],f=0;f<e.length;f++){var h=Ib(e[f]);if(2===h)return null;
if(1===h)return!1}return!0},Jb=function(a){var b=[];return function(c){void 0===b[c]&&(b[c]=Gb(ub[c],a));return b[c]}};/*
 Copyright (c) 2014 Derek Brans, MIT license https://github.com/krux/postscribe/blob/master/LICENSE. Portions derived from simplehtmlparser, which is licensed under the Apache License, Version 2.0 */
var C={ab:"_ee",Mc:"_syn",Lh:"_uei",Jh:"_pci",Ac:"event_callback",Jb:"event_timeout",V:"gtag.config",fa:"allow_ad_personalization_signals",Bc:"restricted_data_processing",Za:"allow_google_signals",ia:"cookie_expires",Ib:"cookie_update",$a:"session_duration",la:"user_properties",xa:"transport_url",M:"ads_data_redaction"};C.Fe=[C.fa,C.Za,C.Ib];C.Je=[C.ia,C.Jb,C.$a];C.m="ad_storage",C.I="analytics_storage",C.uh="region",C.xh="wait_for_update";var fc={},gc=function(a,b){fc[a]=fc[a]||[];fc[a][b]=!0},hc=function(a){for(var b=[],c=fc[a]||[],d=0;d<c.length;d++)c[d]&&(b[Math.floor(d/6)]^=1<<d%6);for(var e=0;e<b.length;e++)b[e]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(b[e]||0);return b.join("")};var D=function(a){gc("GTM",a)};var F=window,H=document,ic=navigator,jc=H.currentScript&&H.currentScript.src,kc=function(a,b){var c=F[a];F[a]=void 0===c?b:c;return F[a]},lc=function(a,b){b&&(a.addEventListener?a.onload=b:a.onreadystatechange=function(){a.readyState in{loaded:1,complete:1}&&(a.onreadystatechange=null,b())})},mc=function(a,b,c){var d=H.createElement("script");d.type="text/javascript";d.async=!0;d.src=a;lc(d,b);c&&(d.onerror=c);var e;if(null===oa)b:{var f=ka.document,h=f.querySelector&&f.querySelector("script[nonce]");
if(h){var k=h.nonce||h.getAttribute("nonce");if(k&&ma.test(k)){oa=k;break b}}oa=""}e=oa;e&&d.setAttribute("nonce",e);var l=H.getElementsByTagName("script")[0]||H.body||H.head;l.parentNode.insertBefore(d,l);return d},nc=function(){if(jc){var a=jc.toLowerCase();if(0===a.indexOf("https://"))return 2;if(0===a.indexOf("http://"))return 3}return 1},oc=function(a,b){var c=H.createElement("iframe");c.height="0";c.width="0";c.style.display="none";c.style.visibility="hidden";var d=H.body&&H.body.lastChild||
H.body||H.head;d.parentNode.insertBefore(c,d);lc(c,b);void 0!==a&&(c.src=a);return c},pc=function(a,b,c){var d=new Image(1,1);d.onload=function(){d.onload=null;b&&b()};d.onerror=function(){d.onerror=null;c&&c()};d.src=a;return d},qc=function(a,b,c,d){a.addEventListener?a.addEventListener(b,c,!!d):a.attachEvent&&a.attachEvent("on"+b,c)},rc=function(a,b,c){a.removeEventListener?a.removeEventListener(b,c,!1):a.detachEvent&&a.detachEvent("on"+b,c)},I=function(a){F.setTimeout(a,0)},sc=function(a,b){return a&&
b&&a.attributes&&a.attributes[b]?a.attributes[b].value:null},tc=function(a){var b=a.innerText||a.textContent||"";b&&" "!=b&&(b=b.replace(/^[\s\xa0]+|[\s\xa0]+$/g,""));b&&(b=b.replace(/(\xa0+|\s{2,}|\n|\r\t)/g," "));return b},uc=function(a){var b=H.createElement("div");b.innerHTML="A<div>"+a+"</div>";b=b.lastChild;for(var c=[];b.firstChild;)c.push(b.removeChild(b.firstChild));return c},vc=function(a,b,c){c=c||100;for(var d={},e=0;e<b.length;e++)d[b[e]]=!0;for(var f=a,h=0;f&&h<=c;h++){if(d[String(f.tagName).toLowerCase()])return f;
f=f.parentElement}return null},wc=function(a){ic.sendBeacon&&ic.sendBeacon(a)||pc(a)},xc=function(a,b){var c=a[b];c&&"string"===typeof c.animVal&&(c=c.animVal);return c};var zc={},Ac=function(a){return void 0==zc[a]?!1:zc[a]};var Bc=[];function Cc(){var a=kc("google_tag_data",{});a.ics||(a.ics={entries:{},set:Dc,update:Ec,addListener:Fc,notifyListeners:Gc,active:!1});return a.ics}
function Dc(a,b,c,d,e,f){var h=Cc();h.active=!0;if(void 0!=b){var k=h.entries,l=k[a]||{},m=l.region,r=c&&g(c)?c.toUpperCase():void 0;d=d.toUpperCase();e=e.toUpperCase();if(r===e||(r===d?m!==e:!r&&!m)){var q=!!(f&&0<f&&void 0===l.update),u={region:r,initial:"granted"===b,update:l.update,quiet:q};k[a]=u;q&&F.setTimeout(function(){k[a]===u&&u.quiet&&(u.quiet=!1,Hc(a),Gc(),gc("TAGGING",2))},f)}}}
function Ec(a,b){var c=Cc();c.active=!0;if(void 0!=b){var d=Ic(a),e=c.entries,f=e[a]=e[a]||{};f.update="granted"===b;var h=Ic(a);f.quiet?(f.quiet=!1,Hc(a)):h!==d&&Hc(a)}}function Fc(a,b){Bc.push({ne:a,yg:b})}function Hc(a){for(var b=0;b<Bc.length;++b){var c=Bc[b];sa(c.ne)&&-1!==c.ne.indexOf(a)&&(c.Pe=!0)}}function Gc(){for(var a=0;a<Bc.length;++a){var b=Bc[a];if(b.Pe){b.Pe=!1;try{b.yg.call()}catch(c){}}}}
var Ic=function(a){var b=Cc().entries[a]||{};return void 0!==b.update?b.update:void 0!==b.initial?b.initial:void 0},Jc=function(a){return!(Cc().entries[a]||{}).quiet},Kc=function(){return Ac("gtag_cs_api")?Cc().active:!1},Lc=function(a,b){Cc().addListener(a,b)},Mc=function(a,b){function c(){for(var e=0;e<b.length;e++)if(!Jc(b[e]))return!0;return!1}if(c()){var d=!1;Lc(b,function(){d||c()||(d=!0,a())})}else a()},Nc=function(a,b){if(!1===Ic(b)){var c=!1;Lc([b],function(){!c&&Ic(b)&&(a(),c=!0)})}};var Oc=[C.m,C.I],Pc=function(a){var b=a[C.uh];b&&D(40);var c=a[C.xh];c&&D(41);for(var d=sa(b)?b:[b],e=0;e<d.length;++e)for(var f=0;f<Oc.length;f++){var h=Oc[f],k=a[Oc[f]],l=d[e];Cc().set(h,k,l,"US","US-CO",c)}},Qc=function(a){for(var b=0;b<Oc.length;b++){var c=Oc[b],d=a[Oc[b]];Cc().update(c,d)}Cc().notifyListeners()},Rc=function(a){var b=Ic(a);return void 0!=b?b:!0},Sc=function(){for(var a=[],b=0;b<Oc.length;b++){var c=Ic(Oc[b]);a[b]=!0===c?"1":!1===c?"0":"-"}return"G1"+a.join("")},
Tc=function(a,b){Mc(a,b)};var Vc=function(a){return Uc?H.querySelectorAll(a):null},Wc=function(a,b){if(!Uc)return null;if(Element.prototype.closest)try{return a.closest(b)}catch(e){return null}var c=Element.prototype.matches||Element.prototype.webkitMatchesSelector||Element.prototype.mozMatchesSelector||Element.prototype.msMatchesSelector||Element.prototype.oMatchesSelector,d=a;if(!H.documentElement.contains(d))return null;do{try{if(c.call(d,b))return d}catch(e){break}d=d.parentElement||d.parentNode}while(null!==d&&1===d.nodeType);
return null},Xc=!1;if(H.querySelectorAll)try{var Yc=H.querySelectorAll(":root");Yc&&1==Yc.length&&Yc[0]==H.documentElement&&(Xc=!0)}catch(a){}var Uc=Xc;var md={},K=null,nd=Math.random();md.s="GTM-KGQ2KV2";md.Ob="7f0";md.Md="";var od={__cl:!0,__ecl:!0,__ehl:!0,__evl:!0,__fal:!0,__fil:!0,__fsl:!0,__hl:!0,__jel:!0,__lcl:!0,__sdl:!0,__tl:!0,__ytl:!0,__paused:!0,__tg:!0},pd="www.googletagmanager.com/gtm.js";
var qd=pd,rd=null,sd=null,td="//www.googletagmanager.com/a?id="+md.s+"&cv=284",ud={},vd={},wd=function(){var a=K.sequence||1;K.sequence=a+1;return a};
var xd=function(){return"&tc="+vb.filter(function(a){return a}).length},Ad=function(){yd||(yd=F.setTimeout(zd,500))},zd=function(){yd&&(F.clearTimeout(yd),yd=void 0);void 0===Bd||Cd[Bd]&&!Dd&&!Ed||(Fd[Bd]||Gd.Og()||0>=Hd--?(D(1),Fd[Bd]=!0):(Gd.kh(),pc(Id()),Cd[Bd]=!0,Jd=Kd=Ed=Dd=""))},Id=function(){var a=Bd;if(void 0===a)return"";var b=hc("GTM"),c=hc("TAGGING");return[Ld,Cd[a]?"":"&es=1",Md[a],b?"&u="+b:"",c?"&ut="+c:"",xd(),Dd,Ed,Kd,Jd,"&z=0"].join("")},Nd=function(){return[td,"&v=3&t=t","&pid="+
va(),"&rv="+md.Ob].join("")},Od="0.005000">Math.random(),Ld=Nd(),Pd=function(){Ld=Nd()},Cd={},Dd="",Ed="",Jd="",Kd="",Bd=void 0,Md={},Fd={},yd=void 0,Gd=function(a,b){var c=0,d=0;return{Og:function(){if(c<a)return!1;Ga()-d>=b&&(c=0);return c>=a},kh:function(){Ga()-d>=b&&(c=0);c++;d=Ga()}}}(2,1E3),Hd=1E3,Qd=function(a,b){if(Od&&!Fd[a]&&Bd!==a){zd();Bd=a;Jd=Dd="";var c;c=0===b.indexOf("gtm.")?encodeURIComponent(b):"*";Md[a]="&e="+c+"&eid="+a;Ad()}},Rd=function(a,b,c){if(Od&&!Fd[a]&&
b){a!==Bd&&(zd(),Bd=a);var d,e=String(b[Hb.Ha]||"").replace(/_/g,"");0===e.indexOf("cvt")&&(e="cvt");d=e;var f=c+d;Dd=Dd?Dd+"."+f:"&tr="+f;var h=b["function"];if(!h)throw Error("Error: No function name given for function call.");var k=(xb[h]?"1":"2")+d;Jd=Jd?Jd+"."+k:"&ti="+k;Ad();2022<=Id().length&&zd()}},Sd=function(a,b,c){if(Od&&!Fd[a]){a!==Bd&&(zd(),Bd=a);var d=c+b;Ed=Ed?Ed+
"."+d:"&epr="+d;Ad();2022<=Id().length&&zd()}};var Td={},Ud=new wa,Vd={},Wd={},Zd={name:"purData",set:function(a,b){n(Ma(a,b),Vd);Xd()},get:function(a){return Yd(a,2)},reset:function(){Ud=new wa;Vd={};Xd()}},Yd=function(a,b){if(2!=b){var c=Ud.get(a);Od&&c!==$d(a.split("."))&&D(5);return c}return $d(a.split("."))},$d=function(a){for(var b=Vd,c=0;c<a.length;c++){if(null===b)return!1;if(void 0===b)break;b=b[a[c]]}return b},ae=function(a,b){Wd.hasOwnProperty(a)||(Ud.set(a,b),n(Ma(a,b),Vd),Xd())},Xd=function(a){Aa(Wd,function(b,c){Ud.set(b,c);
n(Ma(b,void 0),Vd);n(Ma(b,c),Vd);a&&delete Wd[b]})},be=function(a,b,c){Td[a]=Td[a]||{};var d=1!==c?$d(b.split(".")):Ud.get(b);"array"===Pa(d)||"object"===Pa(d)?Td[a][b]=n(d):Td[a][b]=d},ce=function(a,b){if(Td[a])return Td[a][b]},de=function(a,b){Td[a]&&delete Td[a][b]};var ge=/:[0-9]+$/,he=function(a,b,c){for(var d=a.split("&"),e=0;e<d.length;e++){var f=d[e].split("=");if(decodeURIComponent(f[0]).replace(/\+/g," ")===b){var h=f.slice(1).join("=");return c?h:decodeURIComponent(h).replace(/\+/g," ")}}},ke=function(a,b,c,d,e){b&&(b=String(b).toLowerCase());if("protocol"===b||"port"===b)a.protocol=ie(a.protocol)||ie(F.location.protocol);"port"===b?a.port=String(Number(a.hostname?a.port:F.location.port)||("http"==a.protocol?80:"https"==a.protocol?443:"")):"host"===b&&
(a.hostname=(a.hostname||F.location.hostname).replace(ge,"").toLowerCase());return je(a,b,c,d,e)},je=function(a,b,c,d,e){var f,h=ie(a.protocol);b&&(b=String(b).toLowerCase());switch(b){case "url_no_fragment":f=le(a);break;case "protocol":f=h;break;case "host":f=a.hostname.replace(ge,"").toLowerCase();if(c){var k=/^www\d*\./.exec(f);k&&k[0]&&(f=f.substr(k[0].length))}break;case "port":f=String(Number(a.port)||("http"==h?80:"https"==h?443:""));break;case "path":a.pathname||a.hostname||gc("TAGGING",
1);f="/"==a.pathname.substr(0,1)?a.pathname:"/"+a.pathname;var l=f.split("/");0<=ta(d||[],l[l.length-1])&&(l[l.length-1]="");f=l.join("/");break;case "query":f=a.search.replace("?","");e&&(f=he(f,e,void 0));break;case "extension":var m=a.pathname.split(".");f=1<m.length?m[m.length-1]:"";f=f.split("/")[0];break;case "fragment":f=a.hash.replace("#","");break;default:f=a&&a.href}return f},ie=function(a){return a?a.replace(":","").toLowerCase():""},le=function(a){var b="";if(a&&a.href){var c=a.href.indexOf("#");
b=0>c?a.href:a.href.substr(0,c)}return b},me=function(a){var b=H.createElement("a");a&&(b.href=a);var c=b.pathname;"/"!==c[0]&&(a||gc("TAGGING",1),c="/"+c);var d=b.hostname.replace(ge,"");return{href:b.href,protocol:b.protocol,host:b.host,hostname:d,pathname:c,search:b.search,hash:b.hash,port:b.port}},ne=function(a){function b(m){var r=m.split("=")[0];return 0>d.indexOf(r)?m:r+"=0"}function c(m){return m.split("&").map(b).filter(function(r){return void 0!=r}).join("&")}var d="gclid dclid gclaw gcldc gclgp gclha gclgf _gl".split(" "),
e=me(a),f=a.split(/[?#]/)[0],h=e.search,k=e.hash;"?"===h[0]&&(h=h.substring(1));"#"===k[0]&&(k=k.substring(1));h=c(h);k=c(k);""!==h&&(h="?"+h);""!==k&&(k="#"+k);var l=""+f+h+k;"/"===l[l.length-1]&&(l=l.substring(0,l.length-1));return l};function oe(a,b,c){for(var d=[],e=b.split(";"),f=0;f<e.length;f++){var h=e[f].split("="),k=h[0].replace(/^\s*|\s*$/g,"");if(k&&k==a){var l=h.slice(1).join("=").replace(/^\s*|\s*$/g,"");l&&c&&(l=decodeURIComponent(l));d.push(l)}}return d};var qe=function(a,b,c,d){return pe(d)?oe(a,String(b||document.cookie),c):[]},te=function(a,b,c,d,e){if(pe(e)){var f=re(a,d,e);if(1===f.length)return f[0].id;if(0!==f.length){f=se(f,function(h){return h.Tb},b);if(1===f.length)return f[0].id;f=se(f,function(h){return h.yb},c);return f[0]?f[0].id:void 0}}};function ue(a,b,c,d){var e=document.cookie;document.cookie=a;var f=document.cookie;return e!=f||void 0!=c&&0<=qe(b,f,!1,d).indexOf(c)}
var ye=function(a,b,c){function d(p,t,v){if(null==v)return delete h[t],p;h[t]=v;return p+"; "+t+"="+v}function e(p,t){if(null==t)return delete h[t],p;h[t]=!0;return p+"; "+t}if(!pe(c.Ca))return 2;var f;void 0==b?f=a+"=deleted; expires="+(new Date(0)).toUTCString():(c.encode&&(b=encodeURIComponent(b)),b=ve(b),f=a+"="+b);var h={};f=d(f,"path",c.path);var k;c.expires instanceof Date?k=c.expires.toUTCString():null!=c.expires&&(k=""+c.expires);f=d(f,"expires",k);f=d(f,"max-age",c.Vh);f=d(f,"samesite",
c.$h);c.ai&&(f=e(f,"secure"));var l=c.domain;if("auto"===l){for(var m=we(),r=0;r<m.length;++r){var q="none"!==m[r]?m[r]:void 0,u=d(f,"domain",q);u=e(u,c.flags);if(!xe(q,c.path)&&ue(u,a,b,c.Ca))return 0}return 1}l&&"none"!==l&&(f=d(f,"domain",l));f=e(f,c.flags);return xe(l,c.path)?1:ue(f,a,b,c.Ca)?0:1},ze=function(a,b,c){null==c.path&&(c.path="/");c.domain||(c.domain="auto");return ye(a,b,c)};
function se(a,b,c){for(var d=[],e=[],f,h=0;h<a.length;h++){var k=a[h],l=b(k);l===c?d.push(k):void 0===f||l<f?(e=[k],f=l):l===f&&e.push(k)}return 0<d.length?d:e}function re(a,b,c){for(var d=[],e=qe(a,void 0,void 0,c),f=0;f<e.length;f++){var h=e[f].split("."),k=h.shift();if(!b||-1!==b.indexOf(k)){var l=h.shift();l&&(l=l.split("-"),d.push({id:h.join("."),Tb:1*l[0]||1,yb:1*l[1]||1}))}}return d}
var ve=function(a){a&&1200<a.length&&(a=a.substring(0,1200));return a},Ae=/^(www\.)?google(\.com?)?(\.[a-z]{2})?$/,Be=/(^|\.)doubleclick\.net$/i,xe=function(a,b){return Be.test(document.location.hostname)||"/"===b&&Ae.test(a)},we=function(){var a=[],b=document.location.hostname.split(".");if(4===b.length){var c=b[b.length-1];if(parseInt(c,10).toString()===c)return["none"]}for(var d=b.length-2;0<=d;d--)a.push(b.slice(d).join("."));var e=document.location.hostname;Be.test(e)||Ae.test(e)||a.push("none");
return a},pe=function(a){if(!Ac("gtag_cs_api")||!a||!Kc())return!0;if(!Jc(a))return!1;var b=Ic(a);return null==b?!0:!!b};var Ce=function(){for(var a=ic.userAgent+(H.cookie||"")+(H.referrer||""),b=a.length,c=F.history.length;0<c;)a+=c--^b++;var d=1,e,f,h;if(a)for(d=0,f=a.length-1;0<=f;f--)h=a.charCodeAt(f),d=(d<<6&268435455)+h+(h<<14),e=d&266338304,d=0!=e?d^e>>21:d;return[Math.round(2147483647*Math.random())^d&2147483647,Math.round(Ga()/1E3)].join(".")},Fe=function(a,b,c,d,e){var f=De(b);return te(a,f,Ee(c),d,e)},Ge=function(a,b,c,d){var e=""+De(c),f=Ee(d);1<f&&(e+="-"+f);return[b,e,a].join(".")},De=function(a){if(!a)return 1;
a=0===a.indexOf(".")?a.substr(1):a;return a.split(".").length},Ee=function(a){if(!a||"/"===a)return 1;"/"!==a[0]&&(a="/"+a);"/"!==a[a.length-1]&&(a+="/");return a.split("/").length-1};function He(a,b,c){var d,e=a.wb;null==e&&(e=7776E3);0!==e&&(d=new Date((b||Ga())+1E3*e));return{path:a.path,domain:a.domain,flags:a.flags,encode:!!c,expires:d}};var Ie=["1"],Je={},Ne=function(a){var b=Ke(a.prefix);Je[b]||Le(b,a.path,a.domain)||(Me(b,Ce(),a),Le(b,a.path,a.domain))};function Me(a,b,c){var d=Ge(b,"1",c.domain,c.path),e=He(c);e.Ca="ad_storage";ze(a,d,e)}function Le(a,b,c){var d=Fe(a,b,c,Ie,"ad_storage");d&&(Je[a]=d);return d}function Ke(a){return(a||"_gcl")+"_au"};var Oe=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function Pe(){for(var a=Qe,b={},c=0;c<a.length;++c)b[a[c]]=c;return b}function Re(){var a="ABCDEFGHIJKLMNOPQRSTUVWXYZ";a+=a.toLowerCase()+"0123456789-_";return a+"."}var Qe,Se;function Te(a){Qe=Qe||Re();Se=Se||Pe();for(var b=[],c=0;c<a.length;c+=3){var d=c+1<a.length,e=c+2<a.length,f=a.charCodeAt(c),h=d?a.charCodeAt(c+1):0,k=e?a.charCodeAt(c+2):0,l=f>>2,m=(f&3)<<4|h>>4,r=(h&15)<<2|k>>6,q=k&63;e||(q=64,d||(r=64));b.push(Qe[l],Qe[m],Qe[r],Qe[q])}return b.join("")}
function Ue(a){function b(l){for(;d<a.length;){var m=a.charAt(d++),r=Se[m];if(null!=r)return r;if(!/^[\s\xa0]*$/.test(m))throw Error("Unknown base64 encoding at char: "+m);}return l}Qe=Qe||Re();Se=Se||Pe();for(var c="",d=0;;){var e=b(-1),f=b(0),h=b(64),k=b(64);if(64===k&&-1===e)return c;c+=String.fromCharCode(e<<2|f>>4);64!=h&&(c+=String.fromCharCode(f<<4&240|h>>2),64!=k&&(c+=String.fromCharCode(h<<6&192|k)))}};var Ve;var Ze=function(){var a=We,b=Xe,c=Ye(),d=function(h){a(h.target||h.srcElement||{})},e=function(h){b(h.target||h.srcElement||{})};if(!c.init){qc(H,"mousedown",d);qc(H,"keyup",d);qc(H,"submit",e);var f=HTMLFormElement.prototype.submit;HTMLFormElement.prototype.submit=function(){b(this);f.call(this)};c.init=!0}},$e=function(a,b,c,d,e){var f={callback:a,domains:b,fragment:2===c,placement:c,forms:d,sameHost:e};Ye().decorators.push(f)},af=function(a,b,c){for(var d=Ye().decorators,e={},f=0;f<d.length;++f){var h=
d[f],k;if(k=!c||h.forms)a:{var l=h.domains,m=a,r=!!h.sameHost;if(l&&(r||m!==H.location.hostname))for(var q=0;q<l.length;q++)if(l[q]instanceof RegExp){if(l[q].test(m)){k=!0;break a}}else if(0<=m.indexOf(l[q])||r&&0<=l[q].indexOf(m)){k=!0;break a}k=!1}if(k){var u=h.placement;void 0==u&&(u=h.fragment?2:1);u===b&&Ja(e,h.callback())}}return e},Ye=function(){var a=kc("google_tag_data",{}),b=a.gl;b&&b.decorators||(b={decorators:[]},a.gl=b);return b};var bf=/(.*?)\*(.*?)\*(.*)/,cf=/^https?:\/\/([^\/]*?)\.?cdn\.ampproject\.org\/?(.*)/,df=/^(?:www\.|m\.|amp\.)+/,ef=/([^?#]+)(\?[^#]*)?(#.*)?/;function ff(a){return new RegExp("(.*?)(^|&)"+a+"=([^&]*)&?(.*)")}
var hf=function(a){var b=[],c;for(c in a)if(a.hasOwnProperty(c)){var d=a[c];void 0!==d&&d===d&&null!==d&&"[object Object]"!==d.toString()&&(b.push(c),b.push(Te(String(d))))}var e=b.join("*");return["1",gf(e),e].join("*")},gf=function(a,b){var c=[window.navigator.userAgent,(new Date).getTimezoneOffset(),window.navigator.userLanguage||window.navigator.language,Math.floor((new Date).getTime()/60/1E3)-(void 0===b?0:b),a].join("*"),d;if(!(d=Ve)){for(var e=Array(256),f=0;256>f;f++){for(var h=f,k=0;8>k;k++)h=
h&1?h>>>1^3988292384:h>>>1;e[f]=h}d=e}Ve=d;for(var l=4294967295,m=0;m<c.length;m++)l=l>>>8^Ve[(l^c.charCodeAt(m))&255];return((l^-1)>>>0).toString(36)},kf=function(){return function(a){var b=me(F.location.href),c=b.search.replace("?",""),d=he(c,"_gl",!0)||"";a.query=jf(d)||{};var e=ke(b,"fragment").match(ff("_gl"));a.fragment=jf(e&&e[3]||"")||{}}},lf=function(a){var b=kf(),c=Ye();c.data||(c.data={query:{},fragment:{}},b(c.data));var d={},e=c.data;e&&(Ja(d,e.query),a&&Ja(d,e.fragment));return d},jf=
function(a){var b;b=void 0===b?3:b;try{if(a){var c;a:{for(var d=a,e=0;3>e;++e){var f=bf.exec(d);if(f){c=f;break a}d=decodeURIComponent(d)}c=void 0}var h=c;if(h&&"1"===h[1]){var k=h[3],l;a:{for(var m=h[2],r=0;r<b;++r)if(m===gf(k,r)){l=!0;break a}l=!1}if(l){for(var q={},u=k?k.split("*"):[],p=0;p<u.length;p+=2)q[u[p]]=Ue(u[p+1]);return q}}}}catch(t){}};
function mf(a,b,c,d){function e(r){var q=r,u=ff(a).exec(q),p=q;if(u){var t=u[2],v=u[4];p=u[1];v&&(p=p+t+v)}r=p;var w=r.charAt(r.length-1);r&&"&"!==w&&(r+="&");return r+m}d=void 0===d?!1:d;var f=ef.exec(c);if(!f)return"";var h=f[1],k=f[2]||"",l=f[3]||"",m=a+"="+b;d?l="#"+e(l.substring(1)):k="?"+e(k.substring(1));return""+h+k+l}
function nf(a,b){var c="FORM"===(a.tagName||"").toUpperCase(),d=af(b,1,c),e=af(b,2,c),f=af(b,3,c);if(Ka(d)){var h=hf(d);c?of("_gl",h,a):pf("_gl",h,a,!1)}if(!c&&Ka(e)){var k=hf(e);pf("_gl",k,a,!0)}for(var l in f)if(f.hasOwnProperty(l))a:{var m=l,r=f[l],q=a;if(q.tagName){if("a"===q.tagName.toLowerCase()){pf(m,r,q,void 0);break a}if("form"===q.tagName.toLowerCase()){of(m,r,q);break a}}"string"==typeof q&&mf(m,r,q,void 0)}}
function pf(a,b,c,d){if(c.href){var e=mf(a,b,c.href,void 0===d?!1:d);Oe.test(e)&&(c.href=e)}}
function of(a,b,c){if(c&&c.action){var d=(c.method||"").toLowerCase();if("get"===d){for(var e=c.childNodes||[],f=!1,h=0;h<e.length;h++){var k=e[h];if(k.name===a){k.setAttribute("value",b);f=!0;break}}if(!f){var l=H.createElement("input");l.setAttribute("type","hidden");l.setAttribute("name",a);l.setAttribute("value",b);c.appendChild(l)}}else if("post"===d){var m=mf(a,b,c.action);Oe.test(m)&&(c.action=m)}}}
var We=function(a){try{var b;a:{for(var c=a,d=100;c&&0<d;){if(c.href&&c.nodeName.match(/^a(?:rea)?$/i)){b=c;break a}c=c.parentNode;d--}b=null}var e=b;if(e){var f=e.protocol;"http:"!==f&&"https:"!==f||nf(e,e.hostname)}}catch(h){}},Xe=function(a){try{if(a.action){var b=ke(me(a.action),"host");nf(a,b)}}catch(c){}},qf=function(a,b,c,d){Ze();$e(a,b,"fragment"===c?2:1,!!d,!1)},rf=function(a,b){Ze();$e(a,[je(F.location,"host",!0)],b,!0,!0)},sf=function(){var a=H.location.hostname,b=cf.exec(H.referrer);if(!b)return!1;
var c=b[2],d=b[1],e="";if(c){var f=c.split("/"),h=f[1];e="s"===h?decodeURIComponent(f[2]):decodeURIComponent(h)}else if(d){if(0===d.indexOf("xn--"))return!1;e=d.replace(/-/g,".").replace(/\.\./g,"-")}var k=a.replace(df,""),l=e.replace(df,""),m;if(!(m=k===l)){var r="."+l;m=k.substring(k.length-r.length,k.length)===r}return m},tf=function(a,b){return!1===a?!1:a||b||sf()};var uf=/^\w+$/,vf=/^[\w-]+$/,wf=/^~?[\w-]+$/,xf={aw:"_aw",dc:"_dc",gf:"_gf",ha:"_ha",gp:"_gp"},yf=function(){if(!Ac("gtag_cs_api")||!Kc())return!0;var a=Ic("ad_storage");return null==a?!0:!!a},zf=function(a,b){Jc("ad_storage")?yf()?a():Nc(a,"ad_storage"):b?gc("TAGGING",3):Mc(function(){zf(a,!0)},["ad_storage"])},Cf=function(a){var b=[];if(!H.cookie)return b;var c=qe(a,H.cookie,void 0,"ad_storage");if(!c||0==c.length)return b;for(var d=0;d<c.length;d++){var e=Af(c[d]);e&&-1===ta(b,e)&&b.push(e)}return Bf(b)};
function Df(a){return a&&"string"==typeof a&&a.match(uf)?a:"_gcl"}
var Ff=function(){var a=me(F.location.href),b=ke(a,"query",!1,void 0,"gclid"),c=ke(a,"query",!1,void 0,"gclsrc"),d=ke(a,"query",!1,void 0,"dclid");if(!b||!c){var e=a.hash.replace("#","");b=b||he(e,"gclid",void 0);c=c||he(e,"gclsrc",void 0)}return Ef(b,c,d)},Ef=function(a,b,c){var d={},e=function(f,h){d[h]||(d[h]=[]);d[h].push(f)};d.gclid=a;d.gclsrc=b;d.dclid=c;if(void 0!==a&&a.match(vf))switch(b){case void 0:e(a,"aw");break;case "aw.ds":e(a,"aw");e(a,"dc");break;case "ds":e(a,"dc");break;case "3p.ds":Ac("gtm_3pds")&&
e(a,"dc");break;case "gf":e(a,"gf");break;case "ha":e(a,"ha");break;case "gp":e(a,"gp")}c&&e(c,"dc");return d},Hf=function(a){var b=Ff();zf(function(){return Gf(b,a)})};
function Gf(a,b,c){function d(m,r){var q=If(m,e);q&&(ze(q,r,f),h=!0)}b=b||{};var e=Df(b.prefix);c=c||Ga();var f=He(b,c,!0);f.Ca="ad_storage";var h=!1,k=Math.round(c/1E3),l=function(m){return["GCL",k,m].join(".")};a.aw&&(!0===b.ei?d("aw",l("~"+a.aw[0])):d("aw",l(a.aw[0])));a.dc&&d("dc",l(a.dc[0]));a.gf&&d("gf",l(a.gf[0]));a.ha&&d("ha",l(a.ha[0]));a.gp&&d("gp",l(a.gp[0]));return h}
var Kf=function(a,b){var c=lf(!0);zf(function(){for(var d=Df(b.prefix),e=0;e<a.length;++e){var f=a[e];if(void 0!==xf[f]){var h=If(f,d),k=c[h];if(k){var l=Math.min(Jf(k),Ga()),m;b:{for(var r=l,q=qe(h,H.cookie,void 0,"ad_storage"),u=0;u<q.length;++u)if(Jf(q[u])>r){m=!0;break b}m=!1}if(!m){var p=He(b,l,!0);p.Ca="ad_storage";ze(h,k,p)}}}}Gf(Ef(c.gclid,c.gclsrc),b)})},If=function(a,b){var c=xf[a];if(void 0!==c)return b+c},Jf=function(a){var b=a.split(".");return 3!==b.length||"GCL"!==b[0]?0:1E3*(Number(b[1])||
0)};function Af(a){var b=a.split(".");if(3==b.length&&"GCL"==b[0]&&b[1])return b[2]}
var Lf=function(a,b,c,d,e){if(sa(b)){var f=Df(e),h=function(){for(var k={},l=0;l<a.length;++l){var m=If(a[l],f);if(m){var r=qe(m,H.cookie,void 0,"ad_storage");r.length&&(k[m]=r.sort()[r.length-1])}}return k};zf(function(){qf(h,b,c,d)})}},Bf=function(a){return a.filter(function(b){return wf.test(b)})},Mf=function(a,b){for(var c=Df(b.prefix),d={},e=0;e<a.length;e++)xf[a[e]]&&(d[a[e]]=xf[a[e]]);zf(function(){Aa(d,function(f,h){var k=qe(c+h,H.cookie,void 0,"ad_storage");if(k.length){var l=k[0],m=Jf(l),
r={};r[f]=[Af(l)];Gf(r,b,m)}})})};function Nf(a,b){for(var c=0;c<b.length;++c)if(a[b[c]])return!0;return!1}
var Of=function(){function a(e,f,h){h&&(e[f]=h)}var b=["aw","dc"];if(Kc()){var c=Ff();if(Nf(c,b)){var d={};a(d,"gclid",c.gclid);a(d,"dclid",c.dclid);a(d,"gclsrc",c.gclsrc);rf(function(){return d},3);rf(function(){var e={};return e._up="1",e},1)}}},Pf=function(){var a;if(yf()){for(var b=[],c=H.cookie.split(";"),d=/^\s*_gac_(UA-\d+-\d+)=\s*(.+?)\s*$/,e=0;e<c.length;e++){var f=c[e].match(d);f&&b.push({ud:f[1],value:f[2]})}var h={};if(b&&b.length)for(var k=0;k<b.length;k++){var l=b[k].value.split(".");
"1"==l[0]&&3==l.length&&l[1]&&(h[b[k].ud]||(h[b[k].ud]=[]),h[b[k].ud].push({timestamp:l[1],Ag:l[2]}))}a=h}else a={};return a};var Qf=/^\d+\.fls\.doubleclick\.net$/;function Rf(a,b){Jc(C.m)?Rc(C.m)?a():Nc(a,C.m):b?D(42):Tc(function(){Rf(a,!0)},[C.m])}function Sf(a){var b=me(F.location.href),c=ke(b,"host",!1);if(c&&c.match(Qf)){var d=ke(b,"path").split(a+"=");if(1<d.length)return d[1].split(";")[0].split("?")[0]}}
function Tf(a,b,c){if("aw"==a||"dc"==a){var d=Sf("gcl"+a);if(d)return d.split(".")}var e=Df(b);if("_gcl"==e){c=void 0===c?!0:c;var f=!Rc(C.m)&&c,h;h=Ff()[a]||[];if(0<h.length)return f?["0"]:h}var k=If(a,e);return k?Cf(k):[]}
var Uf=function(a){var b=Sf("gac");if(b)return!Rc(C.m)&&a?"0":decodeURIComponent(b);var c=Pf(),d=[];Aa(c,function(e,f){for(var h=[],k=0;k<f.length;k++)h.push(f[k].Ag);h=Bf(h);h.length&&d.push(e+":"+h.join(","))});return d.join(";")},Vf=function(a,b){var c=Ff().dc||[];Rf(function(){Ne(b);var d=Je[Ke(b.prefix)],e=!1;if(d&&0<c.length){var f=K.joined_au=K.joined_au||{},h=b.prefix||"_gcl";if(!f[h])for(var k=0;k<c.length;k++){var l="https://adservice.google.com/ddm/regclk";l=l+"?gclid="+c[k]+"&auiddc="+d;wc(l);e=f[h]=
!0}}null==a&&(a=e);if(a&&d){var m=Ke(b.prefix),r=Je[m];r&&Me(m,r,b)}})};var Wf=/[A-Z]+/,Xf=/\s/,Yf=function(a){if(g(a)&&(a=Fa(a),!Xf.test(a))){var b=a.indexOf("-");if(!(0>b)){var c=a.substring(0,b);if(Wf.test(c)){for(var d=a.substring(b+1).split("/"),e=0;e<d.length;e++)if(!d[e])return;return{id:a,prefix:c,containerId:c+"-"+d[0],B:d}}}}},$f=function(a){for(var b={},c=0;c<a.length;++c){var d=Yf(a[c]);d&&(b[d.id]=d)}Zf(b);var e=[];Aa(b,function(f,h){e.push(h)});return e};
function Zf(a){var b=[],c;for(c in a)if(a.hasOwnProperty(c)){var d=a[c];"AW"===d.prefix&&d.B[1]&&b.push(d.containerId)}for(var e=0;e<b.length;++e)delete a[b[e]]};var ag=function(){var a=!1;return a};var cg=function(a,b,c,d){return(2===bg()||d||"http:"!=F.location.protocol?a:b)+c},bg=function(){var a=nc(),b;if(1===a)a:{var c=qd;c=c.toLowerCase();for(var d="https://"+c,e="http://"+c,f=1,h=H.getElementsByTagName("script"),k=0;k<h.length&&100>k;k++){var l=h[k].src;if(l){l=l.toLowerCase();if(0===l.indexOf(e)){b=3;break a}1===f&&0===l.indexOf(d)&&(f=2)}}b=f}else b=a;return b};
var rg=function(a){return Rc(C.m)?a:a.replace(/&url=([^&#]+)/,function(b,c){var d=ne(decodeURIComponent(c));return"&url="+encodeURIComponent(d)})};var sg=new RegExp(/^(.*\.)?(google|youtube|blogger|withgoogle)(\.com?)?(\.[a-z]{2})?\.?$/),tg={cl:["ecl"],customPixels:["nonGooglePixels"],ecl:["cl"],ehl:["hl"],hl:["ehl"],html:["customScripts","customPixels","nonGooglePixels","nonGoogleScripts","nonGoogleIframes"],customScripts:["html","customPixels","nonGooglePixels","nonGoogleScripts","nonGoogleIframes"],nonGooglePixels:[],nonGoogleScripts:["nonGooglePixels"],nonGoogleIframes:["nonGooglePixels"]},ug={cl:["ecl"],customPixels:["customScripts","html"],
ecl:["cl"],ehl:["hl"],hl:["ehl"],html:["customScripts"],customScripts:["html"],nonGooglePixels:["customPixels","customScripts","html","nonGoogleScripts","nonGoogleIframes"],nonGoogleScripts:["customScripts","html"],nonGoogleIframes:["customScripts","html","nonGoogleScripts"]},vg="google customPixels customScripts html nonGooglePixels nonGoogleScripts nonGoogleIframes".split(" ");
var xg=function(a){var b;b||(b=Yd("gtm.whitelist"));b&&D(9);
var c=b&&La(Ea(b),tg),d;d||(d=Yd("gtm.blacklist"));d||(d=Yd("tagTypeBlacklist"))&&D(3);d?D(8):d=[];wg()&&(d=Ea(d),d.push("nonGooglePixels","nonGoogleScripts","sandboxedScripts"));0<=ta(Ea(d),"google")&&D(2);var e=d&&La(Ea(d),ug),f={};return function(h){var k=
h&&h[Hb.Ha];if(!k||"string"!=typeof k)return!0;k=k.replace(/^_*/,"");if(void 0!==f[k])return f[k];var l=vd[k]||[],m=a(k,l);if(b){var r;if(r=m)a:{if(0>ta(c,k))if(l&&0<l.length)for(var q=0;q<l.length;q++){if(0>ta(c,l[q])){D(11);r=!1;break a}}else{r=!1;break a}r=!0}m=r}var u=!1;if(d){var p=0<=ta(e,k);if(p)u=p;else{var t=ya(e,l||[]);t&&D(10);u=t}}var v=!m||u;v||!(0<=ta(l,"sandboxedScripts"))||c&&-1!==ta(c,"sandboxedScripts")||(v=ya(e,vg));return f[k]=v}},wg=function(){return sg.test(F.location&&F.location.hostname)};var yg={lg:function(a,b){b[Hb.Ed]&&"string"===typeof a&&(a=1==b[Hb.Ed]?a.toLowerCase():a.toUpperCase());b.hasOwnProperty(Hb.Gd)&&null===a&&(a=b[Hb.Gd]);b.hasOwnProperty(Hb.Id)&&void 0===a&&(a=b[Hb.Id]);b.hasOwnProperty(Hb.Hd)&&!0===a&&(a=b[Hb.Hd]);b.hasOwnProperty(Hb.Fd)&&!1===a&&(a=b[Hb.Fd]);return a}};var zg={active:!0,isAllowed:function(){return!0},isWhitelisted:function(){return!0}},Ag=function(a){var b=K.zones;!b&&a&&(b=K.zones=a());return b};var Bg=function(){};var Cg=!1,Dg=0,Eg=[];function Fg(a){if(!Cg){var b=H.createEventObject,c="complete"==H.readyState,d="interactive"==H.readyState;if(!a||"readystatechange"!=a.type||c||!b&&d){Cg=!0;for(var e=0;e<Eg.length;e++)I(Eg[e])}Eg.push=function(){for(var f=0;f<arguments.length;f++)I(arguments[f]);return 0}}}function Gg(){if(!Cg&&140>Dg){Dg++;try{H.documentElement.doScroll("left"),Fg()}catch(a){F.setTimeout(Gg,50)}}}var Hg=function(a){Cg?a():Eg.push(a)};var Ig={},Jg={},Kg=function(a,b,c,d){if(!Jg[a]||od[b]||"__zone"===b)return-1;var e={};Ra(d)&&(e=n(d,e));e.id=c;e.status="timeout";return Jg[a].tags.push(e)-1},Lg=function(a,b,c,d){if(Jg[a]){var e=Jg[a].tags[b];e&&(e.status=c,e.executionTime=d)}};function Mg(a){for(var b=Ig[a]||[],c=0;c<b.length;c++)b[c]();Ig[a]={push:function(d){d(md.s,Jg[a])}}}
var Pg=function(a,b,c){Jg[a]={tags:[]};qa(b)&&Ng(a,b);c&&F.setTimeout(function(){return Mg(a)},Number(c));return Og(a)},Ng=function(a,b){Ig[a]=Ig[a]||[];Ig[a].push(Ia(function(){return I(function(){b(md.s,Jg[a])})}))};function Og(a){var b=0,c=0,d=!1;return{add:function(){c++;return Ia(function(){b++;d&&b>=c&&Mg(a)})},Zf:function(){d=!0;b>=c&&Mg(a)}}};var Qg=function(){function a(d){return!ra(d)||0>d?0:d}if(!K._li&&F.performance&&F.performance.timing){var b=F.performance.timing.navigationStart,c=ra(Zd.get("gtm.start"))?Zd.get("gtm.start"):0;K._li={cst:a(c-b),cbt:a(sd-b)}}};var Ug={},Vg=function(){return F.GoogleAnalyticsObject&&F[F.GoogleAnalyticsObject]},Wg=!1;
var Xg=function(a){F.GoogleAnalyticsObject||(F.GoogleAnalyticsObject=a||"ga");var b=F.GoogleAnalyticsObject;if(F[b])F.hasOwnProperty(b)||D(12);else{var c=function(){c.q=c.q||[];c.q.push(arguments)};c.l=Number(new Date);F[b]=c}Qg();return F[b]},Yg=function(a,b,c,d){b=String(b).replace(/\s+/g,"").split(",");var e=Vg();e(a+"require","linker");e(a+"linker:autoLink",b,c,d)};
var $g=function(a){},Zg=function(){return F.GoogleAnalyticsObject||"ga"};
var ah=function(a,b){return function(){var c=Vg(),d=c&&c.getByName&&c.getByName(a);if(d){var e=d.get("sendHitTask");d.set("sendHitTask",function(f){var h=f.get("hitPayload"),k=f.get("hitCallback"),l=0>h.indexOf("&tid="+b);l&&(f.set("hitPayload",h.replace(/&tid=UA-[0-9]+-[0-9]+/,"&tid="+b),!0),f.set("hitCallback",void 0,!0));e(f);l&&(f.set("hitPayload",h,!0),f.set("hitCallback",k,!0),f.set("_x_19",void 0,!0),e(f))})}}};function fh(a,b,c,d){var e=vb[a],f=gh(a,b,c,d);if(!f)return null;var h=Cb(e[Hb.Vd],c,[]);if(h&&h.length){var k=h[0];f=fh(k.index,{D:f,C:1===k.te?b.terminate:f,terminate:b.terminate},c,d)}return f}
function gh(a,b,c,d){function e(){if(f[Hb.tf])k();else{var w=Eb(f,c,[]),y=Kg(c.id,String(f[Hb.Ha]),Number(f[Hb.Xd]),w[Hb.uf]),x=!1;w.vtp_gtmOnSuccess=function(){if(!x){x=!0;var z=Ga()-B;Rd(c.id,vb[a],"5");Lg(c.id,y,"success",z);h()}};w.vtp_gtmOnFailure=function(){if(!x){x=!0;var z=Ga()-B;Rd(c.id,vb[a],"6");Lg(c.id,y,"failure",z);k()}};w.vtp_gtmTagId=f.tag_id;
w.vtp_gtmEventId=c.id;Rd(c.id,f,"1");var A=function(){var z=Ga()-B;Rd(c.id,f,"7");Lg(c.id,y,"exception",z);x||(x=!0,k())};var B=Ga();try{Bb(w,c)}catch(z){A(z)}}}var f=vb[a],h=b.D,k=b.C,l=b.terminate;if(c.$c(f))return null;var m=Cb(f[Hb.Yd],c,[]);if(m&&m.length){var r=m[0],q=fh(r.index,{D:h,C:k,terminate:l},c,d);if(!q)return null;h=q;k=2===r.te?l:q}if(f[Hb.Nd]||f[Hb.yf]){var u=f[Hb.Nd]?wb:c.sh,p=h,t=k;if(!u[a]){e=Ia(e);var v=hh(a,u,e);h=v.D;k=v.C}return function(){u[a](p,t)}}return e}
function hh(a,b,c){var d=[],e=[];b[a]=ih(d,e,c);return{D:function(){b[a]=jh;for(var f=0;f<d.length;f++)d[f]()},C:function(){b[a]=kh;for(var f=0;f<e.length;f++)e[f]()}}}function ih(a,b,c){return function(d,e){a.push(d);b.push(e);c()}}function jh(a){a()}function kh(a,b){b()};var nh=function(a,b){for(var c=[],d=0;d<vb.length;d++)if(a.xb[d]){var e=vb[d];var f=b.add();try{var h=fh(d,{D:f,C:f,terminate:f},a,d);h?c.push({Ye:d,Qe:Fb(e),wg:h}):(lh(d,a),f())}catch(l){f()}}b.Zf();c.sort(mh);for(var k=0;k<c.length;k++)c[k].wg();return 0<c.length};function mh(a,b){var c,d=b.Qe,e=a.Qe;c=d>e?1:d<e?-1:0;var f;if(0!==c)f=c;else{var h=a.Ye,k=b.Ye;f=h>k?1:h<k?-1:0}return f}
function lh(a,b){if(!Od)return;var c=function(d){var e=b.$c(vb[d])?"3":"4",f=Cb(vb[d][Hb.Vd],b,[]);f&&f.length&&c(f[0].index);Rd(b.id,vb[d],e);var h=Cb(vb[d][Hb.Yd],b,[]);h&&h.length&&c(h[0].index)};c(a);}
var oh=!1,ph=function(a,b,c,d,e){if("gtm.js"==b){if(oh)return!1;oh=!0}Qd(a,b);var f=Pg(a,d,e);be(a,"event",1);be(a,"ecommerce",1);be(a,"gtm");var h={id:a,name:b,$c:xg(c),xb:[],sh:[],He:function(){D(6)}};h.xb=Lb(h);
var k=nh(h,f);"gtm.js"!==b&&"gtm.sync"!==b||$g(md.s);if(!k)return k;for(var l=0;l<h.xb.length;l++)if(h.xb[l]){var m=vb[l];if(m&&!od[String(m[Hb.Ha])])return!0}return!1};function qh(a,b){if(a){var c=""+a;0!==c.indexOf("http://")&&0!==c.indexOf("https://")&&(c="https://"+c);"/"===c[c.length-1]&&(c=c.substring(0,c.length-1));return me(""+c+b).href}}function rh(a,b){return sh()?qh(a,b):void 0}
function sh(){var a=!1;return a};var th=function(){this.eventModel={};this.targetConfig={};this.containerConfig={};this.h={};this.globalConfig={};this.D=function(){};this.C=function(){};this.eventId=void 0},uh=function(a){var b=new th;b.eventModel=a;return b},vh=function(a,b){a.targetConfig=b;return a},wh=function(a,b){a.containerConfig=b;return a},xh=function(a,b){a.h=b;return a},yh=function(a,b){a.globalConfig=b;return a},zh=function(a,b){a.D=b;return a},Ah=function(a,b){a.C=b;return a};
th.prototype.getWithConfig=function(a){if(void 0!==this.eventModel[a])return this.eventModel[a];if(void 0!==this.targetConfig[a])return this.targetConfig[a];if(void 0!==this.containerConfig[a])return this.containerConfig[a];if(void 0!==this.h[a])return this.h[a];if(void 0!==this.globalConfig[a])return this.globalConfig[a]};
var Bh=function(a){function b(e){Aa(e,function(f){c[f]=null})}var c={};b(a.eventModel);b(a.targetConfig);b(a.containerConfig);b(a.globalConfig);var d=[];Aa(c,function(e){d.push(e)});return d};var Ch;if(3===md.Ob.length)Ch="g";else{var Dh="G";Ch=Dh}
var Eh={"":"n",UA:"u",AW:"a",DC:"d",G:"e",GF:"f",HA:"h",GTM:Ch,OPT:"o"},Fh=function(a){var b=md.s.split("-"),c=b[0].toUpperCase(),d=Eh[c]||"i",e=a&&"GTM"===c?b[1]:"OPT"===c?b[1]:"",f;if(3===md.Ob.length){var h="w";f="2"+h}else f="";return f+d+md.Ob+e};function Gh(){var a=!1;a=Kc();return a}
function Hh(a,b,c){function d(q){var u;K.reported_gclid||(K.reported_gclid={});u=K.reported_gclid;var p=f+(q?"gcu":"gcs");if(!u[p]){u[p]=!0;var t=[],v=function(B,z){z&&t.push(B+"="+encodeURIComponent(z))},w="https://www.google.com";if(Kc()){var y=Rc(C.m);v("gcs",Sc());q&&v("gcu","1");v("rnd",r);if((!f||h&&"aw.ds"!==h)&&Rc(C.m)){var x=Cf("_gcl_aw");v("gclaw",x.join("."))}v("url",String(F.location).split(/[?#]/)[0]);v("dclid",Ih(b,k));!y&&b&&(w="https://pagead2.googlesyndication.com")}
"1"===lf(!1)._up&&v("gtm_up","1");v("gclid",Ih(b,f));v("gclsrc",h);v("gtm",Fh(!c));var A=w+"/pagead/landing?"+t.join("&");wc(A)}}var e=Ff(),f=e.gclid||"",h=e.gclsrc,k=e.dclid||"",l=!a&&(!f||h&&"aw.ds"!==h?!1:!0),m=Gh();if(l||m){var r=""+Ce();m?Tc(function(){d();Rc(C.m)||Nc(function(){return d(!0)},C.m)},[C.m]):d()}}function Ih(a,b){var c=a&&!Rc(C.m);if(b&&c)return"0";return b}var Jh=function(a,b){var c=function(){};c.prototype=a.prototype;var d=new c;a.apply(d,Array.prototype.slice.call(arguments,1));return d};var Kh=function(a,b){a.addEventListener&&a.addEventListener("message",b,!1)};var Lh;a:{var Mh=ka.navigator;if(Mh){var Nh=Mh.userAgent;if(Nh){Lh=Nh;break a}}Lh=""}var Oh=function(a){return-1!=Lh.indexOf(a)};var Ph=function(){return Oh("iPhone")&&!Oh("iPod")&&!Oh("iPad")};Oh("Opera");Oh("Trident")||Oh("MSIE");Oh("Edge");!Oh("Gecko")||-1!=Lh.toLowerCase().indexOf("webkit")&&!Oh("Edge")||Oh("Trident")||Oh("MSIE")||Oh("Edge");-1!=Lh.toLowerCase().indexOf("webkit")&&!Oh("Edge")&&Oh("Mobile");Oh("Macintosh");Oh("Windows");Oh("Linux")||Oh("CrOS");var Qh=ka.navigator||null;Qh&&(Qh.appVersion||"").indexOf("X11");Oh("Android");Ph();Oh("iPad");Oh("iPod");Ph()||Oh("iPad")||Oh("iPod");Lh.toLowerCase().indexOf("kaios");var Rh=function(){};var Sh=function(a,b){this.i=a;this.h=null;this.F={};this.ja=0;this.na=void 0===b?500:b;this.o=null};ja(Sh,Rh);
var Uh=function(a,b){var c=setTimeout(function(){c=0;b({tcString:"tcunavailable"})},a.na);Th(a,"addEventListener",function(d){if(d&&(!1===d.gdprApplies||"error"===d.cmpStatus||"loaded"===d.cmpStatus&&("tcloaded"===d.eventStatus||"useractioncomplete"===d.eventStatus))){if(void 0!==d.tcString&&"string"!==typeof d.tcString||void 0!==d.gdprApplies&&"boolean"!==typeof d.gdprApplies||void 0!==d.listenerId&&"number"!==typeof d.listenerId||void 0!==d.addtlConsent&&"string"!==typeof d.addtlConsent||!d.cmpStatus||
"error"===d.cmpStatus)d.tcString="tcunavailable";Th(a,"removeEventListener",null,d.listenerId);c&&(clearTimeout(c),c=0,b(d))}})},Th=function(a,b,c,d){c||(c=function(){});if("function"===typeof a.i.__tcfapi){var e=a.i.__tcfapi;e(b,2,c,d)}else if(Vh(a)){Wh(a);var f=++a.ja;a.F[f]=c;if(a.h){var h={};a.h.postMessage((h.__tcfapiCall={command:b,version:2,callId:f,parameter:d},h),"*")}}else c({},!1)},Vh=function(a){if(a.h)return a.h;var b;a:{for(var c=a.i,d=0;50>d;++d){var e;try{e=!(!c.frames||!c.frames.__tcfapiLocator)}catch(k){e=
!1}if(e){b=c;break a}var f;b:{try{var h=c.parent;if(h&&h!=c){f=h;break b}}catch(k){}f=null}if(!(c=f))break}b=null}a.h=b;return a.h},Wh=function(a){a.o||(a.o=function(b){try{var c,d;"string"===typeof b.data?d=JSON.parse(b.data):d=b.data;c=d.__tcfapiReturn;a.F[c.callId](c.returnValue,c.success)}catch(e){}},Kh(a.i,a.o))};function Xh(){var a=K.tcf||{};return K.tcf=a}var Yh=function(){var a=Xh();if(!a.active){a.active=!0;var b=new Sh(F),c;"function"===typeof F.__tcfapi?c="s":("function"===typeof b.i.__tcfapi||null!=Vh(b))&&(c="i");a.Ge=Ga();try{var d=!1;Uh(b,function(){d=!0;a.dd=Ga()});d&&(a.dd=a.Ge)}catch(e){c="e"}a.type=c}},Zh=function(){var a=Xh();if(a.active&&void 0!==a.dd)return Number(a.dd-a.Ge)};
var ii=function(a){return!(void 0===a||null===a||0===(a+"").length)},ji=function(a,b){var c;if(2===b.X)return a("ord",va(1E11,1E13)),!0;if(3===b.X)return a("ord","1"),a("num",va(1E11,1E13)),!0;if(4===b.X)return ii(b.sessionId)&&a("ord",b.sessionId),!0;if(5===b.X)c="1";else if(6===b.X)c=b.pd;else return!1;ii(c)&&a("qty",c);ii(b.Rb)&&a("cost",b.Rb);ii(b.transactionId)&&a("ord",b.transactionId);return!0},li=function(a,b,c){function d(x,A,B){r.hasOwnProperty(x)||(A=String(A),m.push(";"+x+"="+(B?A:ki(A))))}
var e=a.Tc,f=a.sd,h=a.protocol;h+=f?"//"+e+".fls.doubleclick.net/activityi":"//ad.doubleclick.net/activity";var k=";",l=!Rc(C.m)&&a.zb;l&&(h="https://ade.googlesyndication.com/ddm/activity",k="/",f=!1);var m=[k,"src="+ki(e),";type="+ki(a.Wc),";cat="+ki(a.qb)],r=a.qg||{};Aa(r,function(x,A){m.push(";"+ki(x)+"="+ki(A+""))});if(ji(d,a)){ii(a.vc)&&d("u",a.vc);ii(a.uc)&&d("tran",a.uc);d("gtm",Fh());Kc()&&(d("gcs",Sc()),c&&d("gcu","1"));"1"===lf(!1)._up&&d("gtm_up","1");!1===a.Vf&&d("npa","1");if(a.Sc){var q=
void 0===a.zb?!0:!!a.zb,u=Tf("dc",a.Oa,q);u&&u.length&&d("gcldc",u.join("."));var p=Tf("aw",a.Oa,q);p&&p.length&&d("gclaw",p.join("."));var t=Uf(q);t&&d("gac",t);Ne({prefix:a.Oa,wb:a.ng,domain:a.mg,flags:a.Ph});var v=Je[Ke(a.Oa)];v&&d("auiddc",v)}ii(a.ld)&&d("prd",a.ld,!0);Aa(a.wd,function(x,A){d(x,A)});m.push(b||"");if(ii(a.hc)){var w=a.hc||"";l&&(w=ne(w));d("~oref",w)}var y=h+m.join("")+"?";f?oc(y,a.D):pc(y,a.D,a.C)}else I(a.C)},ki=encodeURIComponent,
mi=function(a,b){Kc()?Tc(function(){li(a,b);Rc(C.m)||Nc(function(){li(a,b,!0)},C.m)},[C.m]):li(a,b)};function cj(){var a=K;return a.gcq=a.gcq||new dj}
var ej=function(a,b,c){cj().register(a,b,c)},fj=function(a,b,c,d){cj().push("event",[b,a],c,d)},gj=function(a,b){cj().push("config",[a],b)},hj={},ij=function(){this.status=1;this.containerConfig={};this.targetConfig={};this.i={};this.o=null;this.h=!1},jj=function(a,b,c,d,e){this.type=a;this.o=b;this.ba=c||"";this.h=d;this.i=e},dj=function(){this.o={};this.i={};this.h=[]},kj=function(a,b){var c=Yf(b);return a.o[c.containerId]=a.o[c.containerId]||new ij},lj=function(a,b,c){if(b){var d=Yf(b);if(d&&1===
kj(a,b).status){kj(a,b).status=2;var e={};Od&&(e.timeoutId=F.setTimeout(function(){D(38);Ad()},3E3));a.push("require",[e],d.containerId);hj[d.containerId]=Ga();if(ag()){
}else{var h="/gtag/js?id="+encodeURIComponent(d.containerId)+"&l=purData&cx=c",k=("http:"!=F.location.protocol?"https:":"http:")+("//www.googletagmanager.com"+h),l=rh(c,h)||k;mc(l)}}}},mj=function(a,b,c,d){if(d.ba){var e=kj(a,d.ba),f=e.o;if(f){var h=n(c),k=n(e.targetConfig[d.ba]),l=n(e.containerConfig),m=n(e.i),r=n(a.i),q=Yd("gtm.uniqueEventId"),u=Yf(d.ba).prefix,p=Ah(zh(yh(xh(wh(vh(uh(h),k),l),m),r),function(){
Sd(q,u,"2");}),function(){Sd(q,u,"3");});try{Sd(q,u,"1");f(d.ba,b,d.o,p)}catch(t){Sd(q,u,"4");}}}};
dj.prototype.register=function(a,b,c){if(3!==kj(this,a).status){kj(this,a).o=b;kj(this,a).status=3;c&&(kj(this,a).i=c);var d=Yf(a),e=hj[d.containerId];if(void 0!==e){var f=K[d.containerId].bootstrap,h=d.prefix.toUpperCase();K[d.containerId]._spx&&(h=h.toLowerCase());var k=Yd("gtm.uniqueEventId"),l=h,m=Ga()-f;if(Od&&!Fd[k]){k!==Bd&&(zd(),Bd=k);var r=l+"."+Math.floor(f-e)+"."+Math.floor(m);Kd=Kd?Kd+","+r:"&cl="+r}delete hj[d.containerId]}this.flush()}};
dj.prototype.push=function(a,b,c,d){var e=Math.floor(Ga()/1E3);lj(this,c,b[0][C.xa]||this.i[C.xa]);this.h.push(new jj(a,e,c,b,d));d||this.flush()};
dj.prototype.flush=function(a){for(var b=this;this.h.length;){var c=this.h[0];if(c.i)c.i=!1,this.h.push(c);else switch(c.type){case "require":if(3!==kj(this,c.ba).status&&!a)return;Od&&F.clearTimeout(c.h[0].timeoutId);break;case "set":Aa(c.h[0],function(l,m){n(Ma(l,m),b.i)});break;case "config":var d=c.h[0],e=!!d[C.jc];delete d[C.jc];var f=kj(this,c.ba),h=Yf(c.ba),k=h.containerId===h.id;e||(k?f.containerConfig={}:f.targetConfig[c.ba]={});f.h&&e||mj(this,C.V,d,c);f.h=!0;delete d[C.ab];k?n(d,f.containerConfig):
n(d,f.targetConfig[c.ba]);break;case "event":mj(this,c.h[1],c.h[0],c)}this.h.shift()}};var nj="HA GF GP G UA AW DC".split(" "),oj=!1,pj={},qj=!1;function rj(a,b){var c={event:a};b&&(c.eventModel=n(b),b[C.Ac]&&(c.eventCallback=b[C.Ac]),b[C.Jb]&&(c.eventTimeout=b[C.Jb]));return c}var tj=function(){return oj};
var vj={config:function(a){},event:function(a){var b=a[1];if(g(b)&&!(3<a.length)){var c;if(2<a.length){if(!Ra(a[2])&&
void 0!=a[2])return;c=a[2]}var d=rj(b,c);return d}},js:function(a){if(2==a.length&&a[1].getTime)return qj=!0,tj(),{event:"gtm.js","gtm.start":a[1].getTime()}},policy:function(){},set:function(a){var b;2==a.length&&Ra(a[1])?b=n(a[1]):3==a.length&&g(a[1])&&(b={},Ra(a[2])||sa(a[2])?b[a[1]]=n(a[2]):b[a[1]]=a[2]);if(b){
b._clear=!0;return b}}};vj.consent=function(a){if(3===a.length){var b=function(){tj()&&n(a[2],{subcommand:a[1]})};D(39);var c=a[1];if("default"===c){b();Pc(a[2]);return}if("update"===c){b();Qc(a[2]);return}}};var wj={policy:!0};var xj=function(a,b){var c=a.hide;if(c&&void 0!==c[b]&&c.end){c[b]=!1;var d=!0,e;for(e in c)if(c.hasOwnProperty(e)&&!0===c[e]){d=!1;break}d&&(c.end(),c.end=null)}},zj=function(a){var b=yj(),c=b&&b.hide;c&&c.end&&(c[a]=!0)};var Aj=!1,Bj=[];function Cj(){if(!Aj){Aj=!0;for(var a=0;a<Bj.length;a++)I(Bj[a])}}var Dj=function(a){Aj?I(a):Bj.push(a)};var Vj=function(a){if(Uj(a))return a;this.h=a};Vj.prototype.Eg=function(){return this.h};var Uj=function(a){return!a||"object"!==Pa(a)||Ra(a)?!1:"getUntrustedUpdateValue"in a};Vj.prototype.getUntrustedUpdateValue=Vj.prototype.Eg;var Wj=[],Xj=!1,Yj=function(a){return F["purData"].push(a)},Zj=function(a){var b=K["purData"],c=b?b.subscribers:1,d=0;return function(){++d===c&&a()}};
function ak(a){var b=a._clear;Aa(a,function(f,h){"_clear"!==f&&(b&&ae(f,void 0),ae(f,h))});rd||(rd=a["gtm.start"]);var c=a.event,d=a["gtm.uniqueEventId"];if(!c)return!1;d||(d=wd(),a["gtm.uniqueEventId"]=d,ae("gtm.uniqueEventId",d));var e=bk(a);switch(c){case "gtm.init":D(19),e&&D(20)}return e}
function bk(a){var b=a.event,c=a["gtm.uniqueEventId"],d,e=K.zones;d=e?e.checkState(md.s,c):zg;return d.active?ph(c,b,d.isAllowed||d.isWhitelist,a.eventCallback,a.eventTimeout)?!0:!1:!1}
function ck(){for(var a=!1;!Xj&&0<Wj.length;){Xj=!0;delete Vd.eventModel;Xd();var b=Wj.shift();if(null!=b){var c=Uj(b);if(c){var d=b;b=Uj(d)?d.getUntrustedUpdateValue():void 0;for(var e=["gtm.allowlist","gtm.blocklist","gtm.whitelist","gtm.blacklist","tagTypeBlacklist"],f=0;f<e.length;f++){var h=e[f],k=Yd(h,1);if(sa(k)||Ra(k))k=n(k);Wd[h]=k}}try{if(qa(b))try{b.call(Zd)}catch(w){}else if(sa(b)){var l=
b;if(g(l[0])){var m=l[0].split("."),r=m.pop(),q=l.slice(1),u=Yd(m.join("."),2);if(void 0!==u&&null!==u)try{u[r].apply(u,q)}catch(w){}}}else{var p=b;if(p&&("[object Arguments]"==Object.prototype.toString.call(p)||Object.prototype.hasOwnProperty.call(p,"callee"))){a:{var t=b;if(t.length&&g(t[0])){var v=vj[t[0]];if(v&&(!c||!wj[t[0]])){b=v(t);break a}}b=void 0}if(!b){Xj=!1;continue}}a=ak(b)||a}}finally{c&&Xd(!0)}}Xj=!1}
return!a}function dk(){var a=ck();try{xj(F["purData"],md.s)}catch(b){}return a}
var fk=function(){var a=kc("purData",[]),b=kc("google_tag_manager",{});b=b["purData"]=b["purData"]||{};Hg(function(){b.gtmDom||(b.gtmDom=!0,a.push({event:"gtm.dom"}))});Dj(function(){b.gtmLoad||(b.gtmLoad=!0,a.push({event:"gtm.load"}))});b.subscribers=(b.subscribers||0)+1;var c=a.push;a.push=function(){var e;if(0<K.SANDBOXED_JS_SEMAPHORE){e=[];for(var f=0;f<arguments.length;f++)e[f]=new Vj(arguments[f])}else e=[].slice.call(arguments,0);var h=c.apply(a,e);Wj.push.apply(Wj,e);if(300<
this.length)for(D(4);300<this.length;)this.shift();var k="boolean"!==typeof h||h;return ck()&&k};var d=a.slice(0);Wj.push.apply(Wj,d);ek()&&I(dk)},ek=function(){var a=!0;return a};var gk={};gk.Kb=new String("undefined");
var hk=function(a){this.h=function(b){for(var c=[],d=0;d<a.length;d++)c.push(a[d]===gk.Kb?b:a[d]);return c.join("")}};hk.prototype.toString=function(){return this.h("undefined")};hk.prototype.valueOf=hk.prototype.toString;gk.Hf=hk;gk.Lc={};gk.og=function(a){return new hk(a)};var ik={};gk.lh=function(a,b){var c=wd();ik[c]=[a,b];return c};gk.oe=function(a){var b=a?0:1;return function(c){var d=ik[c];if(d&&"function"===typeof d[b])d[b]();ik[c]=void 0}};gk.Mg=function(a){for(var b=!1,c=!1,d=2;d<a.length;d++)b=
b||8===a[d],c=c||16===a[d];return b&&c};gk.dh=function(a){if(a===gk.Kb)return a;var b=wd();gk.Lc[b]=a;return'google_tag_manager["'+md.s+'"].macro('+b+")"};gk.Wg=function(a,b,c){a instanceof gk.Hf&&(a=a.h(gk.lh(b,c)),b=pa);return{Yc:a,D:b}};var jk=function(a,b,c){function d(f,h){var k=f[h];return k}var e={event:b,"gtm.element":a,"gtm.elementClasses":d(a,"className"),"gtm.elementId":a["for"]||sc(a,"id")||"","gtm.elementTarget":a.formTarget||d(a,"target")||""};c&&(e["gtm.triggers"]=c.join(","));e["gtm.elementUrl"]=(a.attributes&&a.attributes.formaction?a.formAction:"")||a.action||d(a,"href")||a.src||a.code||a.codebase||
"";return e},kk=function(a){K.hasOwnProperty("autoEventsSettings")||(K.autoEventsSettings={});var b=K.autoEventsSettings;b.hasOwnProperty(a)||(b[a]={});return b[a]},lk=function(a,b,c){kk(a)[b]=c},mk=function(a,b,c,d){var e=kk(a),f=Ha(e,b,d);e[b]=c(f)},nk=function(a,b,c){var d=kk(a);return Ha(d,b,c)};var ok=["input","select","textarea"],pk=["button","hidden","image","reset","submit"],qk=function(a){var b=a.tagName.toLowerCase();return!ua(ok,function(c){return c===b})||"input"===b&&ua(pk,function(c){return c===a.type.toLowerCase()})?!1:!0},rk=function(a){return a.form?a.form.tagName?a.form:H.getElementById(a.form):vc(a,["form"],100)},sk=function(a,b,c){if(!a.elements)return 0;for(var d=b.getAttribute(c),e=0,f=1;e<a.elements.length;e++){var h=a.elements[e];if(qk(h)){if(h.getAttribute(c)===d)return f;
f++}}return 0};var tk=!!F.MutationObserver,uk=void 0,vk=function(a){if(!uk){var b=function(){var c=H.body;if(c)if(tk)(new MutationObserver(function(){for(var e=0;e<uk.length;e++)I(uk[e])})).observe(c,{childList:!0,subtree:!0});else{var d=!1;qc(c,"DOMNodeInserted",function(){d||(d=!0,I(function(){d=!1;for(var e=0;e<uk.length;e++)I(uk[e])}))})}};uk=[];H.body?b():I(b)}uk.push(a)};
var Gk=function(){var a=H.body,b=H.documentElement||a&&a.parentElement,c,d;if(H.compatMode&&"BackCompat"!==H.compatMode)c=b?b.clientHeight:0,d=b?b.clientWidth:0;else{var e=function(f,h){return f&&h?Math.min(f,h):Math.max(f,h)};D(7);c=e(b?b.clientHeight:0,a?a.clientHeight:0);d=e(b?b.clientWidth:0,a?a.clientWidth:0)}return{width:d,height:c}},Hk=function(a){var b=Gk(),c=b.height,d=b.width,e=a.getBoundingClientRect(),f=e.bottom-e.top,h=e.right-e.left;return f&&h?(1-Math.min((Math.max(0-e.left,0)+Math.max(e.right-
d,0))/h,1))*(1-Math.min((Math.max(0-e.top,0)+Math.max(e.bottom-c,0))/f,1)):0},Ik=function(a){if(H.hidden)return!0;var b=a.getBoundingClientRect();if(b.top==b.bottom||b.left==b.right||!F.getComputedStyle)return!0;var c=F.getComputedStyle(a,null);if("hidden"===c.visibility)return!0;for(var d=a,e=c;d;){if("none"===e.display)return!0;var f=e.opacity,h=e.filter;if(h){var k=h.indexOf("opacity(");0<=k&&(h=h.substring(k+8,h.indexOf(")",k)),"%"==h.charAt(h.length-1)&&(h=h.substring(0,h.length-1)),f=Math.min(h,
f))}if(void 0!==f&&0>=f)return!0;(d=d.parentElement)&&(e=F.getComputedStyle(d,null))}return!1};
var Pk=function(a,b,c){function d(){var h=a();f+=e?(Ga()-e)*h.playbackRate/1E3:0;e=Ga()}var e=0,f=0;return{Ub:function(h,k,l){var m=a(),r=m.pe,q=void 0!==l?Math.round(l):void 0!==k?Math.round(m.pe*k):Math.round(m.pg),u=void 0!==k?Math.round(100*k):0>=r?0:Math.round(q/r*100),p=H.hidden?!1:.5<=Hk(c);d();var t=jk(c,"gtm.video",[b]);t["gtm.videoProvider"]="youtube";t["gtm.videoStatus"]=h;t["gtm.videoUrl"]=m.url;t["gtm.videoTitle"]=m.title;t["gtm.videoDuration"]=Math.round(r);t["gtm.videoCurrentTime"]=
Math.round(q);t["gtm.videoElapsedTime"]=Math.round(f);t["gtm.videoPercent"]=u;t["gtm.videoVisible"]=p;Yj(t)},nh:function(){e=Ga()},Nc:function(){d()}}};var Qk=F.clearTimeout,Rk=F.setTimeout,R=function(a,b,c){if(ag()){b&&I(b)}else return mc(a,b,c)},Sk=function(){return F.location.href},Tk=function(a){return ke(me(a),"fragment")},Uk=function(a){return le(me(a))},Vk=function(a,b){return Yd(a,b||2)},Wk=function(a,b,c){var d;b?(a.eventCallback=b,c&&(a.eventTimeout=c),d=Yj(a)):d=Yj(a);return d},Xk=function(a,b){F[a]=b},U=function(a,b,c){b&&(void 0===F[a]||c&&!F[a])&&(F[a]=
b);return F[a]},Yk=function(a,b,c){return qe(a,b,void 0===c?!0:!!c)},Zk=function(a,b){if(ag()){b&&I(b)}else oc(a,b)},$k=function(a){return!!nk(a,"init",!1)},al=function(a){lk(a,"init",!0)},bl=function(a,b){var c=(void 0===b?0:b)?"www.googletagmanager.com/gtag/js":qd;c+="?id="+encodeURIComponent(a)+"&l=purData";R(cg("https://","http://",c))},cl=function(a,b){var c=a[b];return c};
var dl=gk.Wg;function Al(a,b){a=String(a);b=String(b);var c=a.length-b.length;return 0<=c&&a.indexOf(b,c)==c}var Bl=new wa;function Cl(a,b){function c(h){var k=me(h),l=ke(k,"protocol"),m=ke(k,"host",!0),r=ke(k,"port"),q=ke(k,"path").toLowerCase().replace(/\/$/,"");if(void 0===l||"http"==l&&"80"==r||"https"==l&&"443"==r)l="web",r="default";return[l,m,r,q]}for(var d=c(String(a)),e=c(String(b)),f=0;f<d.length;f++)if(d[f]!==e[f])return!1;return!0}
function Dl(a){return El(a)?1:0}
function El(a){var b=a.arg0,c=a.arg1;if(a.any_of&&sa(c)){for(var d=0;d<c.length;d++)if(Dl({"function":a["function"],arg0:b,arg1:c[d]}))return!0;return!1}switch(a["function"]){case "_cn":return 0<=String(b).indexOf(String(c));case "_css":var e;a:{if(b){var f=["matches","webkitMatchesSelector","mozMatchesSelector","msMatchesSelector","oMatchesSelector"];try{for(var h=0;h<f.length;h++)if(b[f[h]]){e=b[f[h]](c);break a}}catch(u){}}e=!1}return e;case "_ew":return Al(b,c);case "_eq":return String(b)==String(c);
case "_ge":return Number(b)>=Number(c);case "_gt":return Number(b)>Number(c);case "_lc":var k;k=String(b).split(",");return 0<=ta(k,String(c));case "_le":return Number(b)<=Number(c);case "_lt":return Number(b)<Number(c);case "_re":var l;var m=a.ignore_case?"i":void 0;try{var r=String(c)+m,q=Bl.get(r);q||(q=new RegExp(c,m),Bl.set(r,q));l=q.test(b)}catch(u){l=!1}return l;case "_sw":return 0==String(b).indexOf(String(c));case "_um":return Cl(b,c)}return!1};var Fl={},Gl=encodeURI,Y=encodeURIComponent,Hl=pc;var Il=function(a,b){if(!a)return!1;var c=ke(me(a),"host");if(!c)return!1;for(var d=0;b&&d<b.length;d++){var e=b[d]&&b[d].toLowerCase();if(e){var f=c.length-e.length;0<f&&"."!=e.charAt(0)&&(f--,e="."+e);if(0<=f&&c.indexOf(e,f)==f)return!0}}return!1};
var Jl=function(a,b,c){for(var d={},e=!1,f=0;a&&f<a.length;f++)a[f]&&a[f].hasOwnProperty(b)&&a[f].hasOwnProperty(c)&&(d[a[f][b]]=a[f][c],e=!0);return e?d:null};Fl.Ng=function(){var a=!1;return a};function bn(){return F.gaGlobal=F.gaGlobal||{}}var cn=function(){var a=bn();a.hid=a.hid||va();return a.hid};var mn=window,nn=document,on=function(a){var b=mn._gaUserPrefs;if(b&&b.ioo&&b.ioo()||a&&!0===mn["ga-disable-"+a])return!0;try{var c=mn.external;if(c&&c._gaUserPrefs&&"oo"==c._gaUserPrefs)return!0}catch(f){}for(var d=oe("AMP_TOKEN",String(nn.cookie),!0),e=0;e<d.length;e++)if("$OPT_OUT"==d[e])return!0;return nn.getElementById("__gaOptOutExtension")?!0:!1};function rn(a,b){delete b.eventModel[C.ab];if(a!==C.V){var c=b.getWithConfig(C.bc);if(sa(c)){D(26);for(var d={},e=0;e<c.length;e++){var f=c[e],h=b.getWithConfig(f);void 0!==h&&(d[f]=h)}b.eventModel=d}}tn(b.eventModel)}var tn=function(a){Aa(a,function(c){"_"===c.charAt(0)&&delete a[c]});var b=a[C.la]||{};Aa(b,function(c){"_"===c.charAt(0)&&delete b[c]})};var wn=function(a,b,c){fj(b,c,a)},xn=function(a,b,c){fj(b,c,a,!0)},zn=function(a,b){};
function yn(a,b){}var Z={a:{}};
Z.a.gaawc=["google"],function(){function a(b,c,d){for(var e=0;e<c.length;e++)b.hasOwnProperty(c[e])&&(b[c[e]]=d(b[c[e]]))}(function(b){Z.__gaawc=b;Z.__gaawc.b="gaawc";Z.__gaawc.g=!0;Z.__gaawc.priorityOverride=10})(function(b){var c=String(b.vtp_measurementId),d=Jl(b.vtp_fieldsToSet,"name","value")||{};if(d.hasOwnProperty(C.la)||b.vtp_userProperties){var e=d[C.la]||{};n(Jl(b.vtp_userProperties,"name","value"),e);d[C.la]=e}a(d,C.Fe,function(f){return Da(f)});a(d,C.Je,function(f){return Number(f)});
d.send_page_view=b.vtp_sendPageView;gj(d,c);I(b.vtp_gtmOnSuccess)})}();
Z.a.sdl=["google"],function(){function a(){return!!(Object.keys(l("horiz.pix")).length||Object.keys(l("horiz.pct")).length||Object.keys(l("vert.pix")).length||Object.keys(l("vert.pct")).length)}function b(x){for(var A=[],B=x.split(","),z=0;z<B.length;z++){var E=Number(B[z]);if(isNaN(E))return[];r.test(B[z])||A.push(E)}return A}function c(){var x=0,A=0;return function(){var B=Gk(),z=B.height;x=Math.max(v.scrollLeft+B.width,x);A=Math.max(v.scrollTop+z,A);return{rg:x,sg:A}}}function d(){p=U("self");
t=p.document;v=t.scrollingElement||t.body&&t.body.parentNode;y=c()}function e(x,A,B,z){var E=l(A),G={},L;for(L in E){G.Ga=L;if(E.hasOwnProperty(G.Ga)){var Q=Number(G.Ga);x<Q||(Wk({event:"gtm.scrollDepth","gtm.scrollThreshold":Q,"gtm.scrollUnits":B.toLowerCase(),"gtm.scrollDirection":z,"gtm.triggers":E[G.Ga].join(",")}),mk("sdl",A,function(S){return function(O){delete O[S.Ga];return O}}(G),{}))}G={Ga:G.Ga}}}function f(){var x=y(),A=x.rg,B=x.sg,z=A/v.scrollWidth*100,E=B/v.scrollHeight*100;e(A,"horiz.pix",
q.Mb,u.Kd);e(z,"horiz.pct",q.Lb,u.Kd);e(B,"vert.pix",q.Mb,u.be);e(E,"vert.pct",q.Lb,u.be);lk("sdl","pending",!1)}function h(){var x=250,A=!1;t.scrollingElement&&t.documentElement&&p.addEventListener&&(x=50,A=!0);var B=0,z=!1,E=function(){z?B=Rk(E,x):(B=0,f(),$k("sdl")&&!a()&&(rc(p,"scroll",G),rc(p,"resize",G),lk("sdl","init",!1)));z=!1},G=function(){A&&y();B?z=!0:(B=Rk(E,x),lk("sdl","pending",!0))};return G}function k(x,A,B){if(A){var z=b(String(x));mk("sdl",B,function(E){for(var G=0;G<z.length;G++){var L=
String(z[G]);E.hasOwnProperty(L)||(E[L]=[]);E[L].push(A)}return E},{})}}function l(x){return nk("sdl",x,{})}function m(x){I(x.vtp_gtmOnSuccess);var A=x.vtp_uniqueTriggerId,B=x.vtp_horizontalThresholdsPixels,z=x.vtp_horizontalThresholdsPercent,E=x.vtp_verticalThresholdUnits,G=x.vtp_verticalThresholdsPixels,L=x.vtp_verticalThresholdsPercent;switch(x.vtp_horizontalThresholdUnits){case q.Mb:k(B,A,"horiz.pix");break;case q.Lb:k(z,A,"horiz.pct")}switch(E){case q.Mb:k(G,A,"vert.pix");break;case q.Lb:k(L,
A,"vert.pct")}$k("sdl")?nk("sdl","pending")||(w||(d(),w=!0),I(function(){return f()})):(d(),w=!0,v&&(al("sdl"),lk("sdl","pending",!0),I(function(){f();if(a()){var Q=h();qc(p,"scroll",Q);qc(p,"resize",Q)}else lk("sdl","init",!1)})))}var r=/^\s*$/,q={Lb:"PERCENT",Mb:"PIXELS"},u={be:"vertical",Kd:"horizontal"},p,t,v,w=!1,y;(function(x){Z.__sdl=x;Z.__sdl.b="sdl";Z.__sdl.g=!0;Z.__sdl.priorityOverride=0})(function(x){x.vtp_triggerStartOption?m(x):Dj(function(){m(x)})})}();

Z.a.jsm=["customScripts"],function(){(function(a){Z.__jsm=a;Z.__jsm.b="jsm";Z.__jsm.g=!0;Z.__jsm.priorityOverride=0})(function(a){if(void 0!==a.vtp_javascript){var b=a.vtp_javascript;try{var c=U("google_tag_manager");return c&&c.e&&c.e(b)}catch(d){}}})}();
Z.a.flc=[],function(){function a(b,c){c=c?c.slice(0,-1):void 0;mi(b,c)}(function(b){Z.__flc=b;Z.__flc.b="flc";Z.__flc.g=!0;Z.__flc.priorityOverride=0})(function(b){var c=!b.hasOwnProperty("vtp_enableConversionLinker")||b.vtp_enableConversionLinker,d=Jl(b.vtp_customVariable||[],"key","value")||{},e={qb:b.vtp_activityTag,Sc:c,Oa:b.vtp_conversionCookiePrefix||void 0,Rb:void 0,X:{UNIQUE:3,SESSION:4}[b.vtp_ordinalType]||2,Tc:b.vtp_advertiserId,Wc:b.vtp_groupTag,C:b.vtp_gtmOnFailure,D:b.vtp_gtmOnSuccess,
hc:b.vtp_useImageTag?void 0:b.vtp_url,protocol:"",pd:void 0,sd:!b.vtp_useImageTag,sessionId:b.vtp_sessionId,uc:b.vtp_transactionVariable,transactionId:void 0,vc:b.vtp_userVariable,wd:d},f=!Rc(C.m)&&void 0!=Vk(C.M)&&!1!==Vk(C.M);e.zb=f;if(b.vtp_enableAttribution){var h=b.vtp_attributionFields||[];if(h.length){R("//www.gstatic.com/attribution/collection/attributiontools.js",function(){a(e,U("google_attr").build([Jl(h,"key","value")||{}]))},b.vtp_gtmOnFailure);return}}a(e)})}();

Z.a.c=["google"],function(){(function(a){Z.__c=a;Z.__c.b="c";Z.__c.g=!0;Z.__c.priorityOverride=0})(function(a){return a.vtp_value})}();
Z.a.e=["google"],function(){(function(a){Z.__e=a;Z.__e.b="e";Z.__e.g=!0;Z.__e.priorityOverride=0})(function(a){return String(ce(a.vtp_gtmEventId,"event"))})}();
Z.a.f=["google"],function(){(function(a){Z.__f=a;Z.__f.b="f";Z.__f.g=!0;Z.__f.priorityOverride=0})(function(a){var b=Vk("gtm.referrer",1)||H.referrer;return b?a.vtp_component&&"URL"!=a.vtp_component?ke(me(String(b)),a.vtp_component,a.vtp_stripWww,a.vtp_defaultPages,a.vtp_queryKey):Uk(String(b)):String(b)})}();
Z.a.cl=["google"],function(){function a(b){var c=b.target;if(c){var d=jk(c,"gtm.click");Wk(d)}}(function(b){Z.__cl=b;Z.__cl.b="cl";Z.__cl.g=!0;Z.__cl.priorityOverride=0})(function(b){if(!$k("cl")){var c=U("document");qc(c,"click",a,!0);al("cl")}I(b.vtp_gtmOnSuccess)})}();
Z.a.j=["google"],function(){(function(a){Z.__j=a;Z.__j.b="j";Z.__j.g=!0;Z.__j.priorityOverride=0})(function(a){for(var b=String(a.vtp_name).split("."),c=U(b.shift()),d=0;d<b.length;d++)c=c&&c[b[d]];return c})}();Z.a.k=["google"],function(){(function(a){Z.__k=a;Z.__k.b="k";Z.__k.g=!0;Z.__k.priorityOverride=0})(function(a){return Yk(a.vtp_name,Vk("gtm.cookie",1),!!a.vtp_decodeCookie)[0]})}();
Z.a.r=["google"],function(){(function(a){Z.__r=a;Z.__r.b="r";Z.__r.g=!0;Z.__r.priorityOverride=0})(function(a){return va(a.vtp_min,a.vtp_max)})}();
Z.a.tg=["google"],function(){function a(k){h.push(k);1<h.length||I(function(){var l=h.join(",");h=[];Wk({event:"gtm.triggerGroup","gtm.triggers":l})})}function b(k,l){var m=d[l],r=m.indexOf(k);-1!==r&&(m.splice(r,1),m.length||a(l))}function c(k){I(k.vtp_gtmOnSuccess);var l=k.vtp_uniqueTriggerId,m=k.vtp_triggerIds,r=k.vtp_firingId;if(k.vtp_isListeningTag){var q=e[r];q?b(r,q):f.push(r)}else{d[l]=m;for(var u=0,p;p=m[u];u++)e[p]=l;for(var t=0;t<f.length;t++)b(f[t],l)}}var d={},e={},f=[],h=[];Z.__tg=c;Z.__tg.b="tg";Z.__tg.g=!0;Z.__tg.priorityOverride=0}();
Z.a.u=["google"],function(){var a=function(b){return{toString:function(){return b}}};(function(b){Z.__u=b;Z.__u.b="u";Z.__u.g=!0;Z.__u.priorityOverride=0})(function(b){var c;b.vtp_customUrlSource?c=b.vtp_customUrlSource:c=Vk("gtm.url",1);c=c||Sk();var d=b[a("vtp_component")];if(!d||"URL"==d)return Uk(String(c));var e=me(String(c)),f;if("QUERY"===d)a:{var h=b[a("vtp_multiQueryKeys").toString()],k=b[a("vtp_queryKey").toString()]||"",l=b[a("vtp_ignoreEmptyQueryParam").toString()],m;h?sa(k)?m=k:m=String(k).replace(/\s+/g,
"").split(","):m=[String(k)];for(var r=0;r<m.length;r++){var q=ke(e,"QUERY",void 0,void 0,m[r]);if(void 0!=q&&(!l||""!==q)){f=q;break a}}f=void 0}else f=ke(e,d,"HOST"==d?b[a("vtp_stripWww")]:void 0,"PATH"==d?b[a("vtp_defaultPages")]:void 0,void 0);return f})}();
Z.a.v=["google"],function(){(function(a){Z.__v=a;Z.__v.b="v";Z.__v.g=!0;Z.__v.priorityOverride=0})(function(a){var b=a.vtp_name;if(!b||!b.replace)return!1;var c=Vk(b.replace(/\\\./g,"."),a.vtp_dataLayerVersion||1);return void 0!==c?c:a.vtp_defaultValue})}();
Z.a.ua=["google"],function(){var a,b={},c=function(e){Tc(function(){d(e)},[C.I,C.m])},d=function(e){var f={},h={},k={},l={},m={};if(e.vtp_gaSettings){var r=e.vtp_gaSettings;n(Jl(r.vtp_fieldsToSet,"fieldName","value"),h);n(Jl(r.vtp_contentGroup,"index","group"),k);n(Jl(r.vtp_dimension,"index","dimension"),l);n(Jl(r.vtp_metric,"index","metric"),m);e.vtp_gaSettings=null;r.vtp_fieldsToSet=void 0;r.vtp_contentGroup=void 0;r.vtp_dimension=void 0;r.vtp_metric=void 0;var q=n(r);e=n(e,q)}n(Jl(e.vtp_fieldsToSet,
"fieldName","value"),h);n(Jl(e.vtp_contentGroup,"index","group"),k);n(Jl(e.vtp_dimension,"index","dimension"),l);n(Jl(e.vtp_metric,"index","metric"),m);Rc(C.I)||(h.storage="none"),Rc(C.m)||(h.allowAdFeatures=!1,h.storeGac=!1);var u=Xg(e.vtp_functionName);if(qa(u)){var p="",t="";e.vtp_setTrackerName&&"string"==typeof e.vtp_trackerName?""!==e.vtp_trackerName&&(t=e.vtp_trackerName,p=t+"."):(t="gtm"+wd(),
p=t+".");var v={name:!0,clientId:!0,sampleRate:!0,siteSpeedSampleRate:!0,alwaysSendReferrer:!0,allowAnchor:!0,allowLinker:!0,cookieName:!0,cookieDomain:!0,cookieExpires:!0,cookiePath:!0,cookieUpdate:!0,cookieFlags:!0,legacyCookieDomain:!0,legacyHistoryImport:!0,storage:!0,useAmpClientId:!0,storeGac:!0,_cd2l:!0},w={allowAnchor:!0,allowLinker:!0,alwaysSendReferrer:!0,anonymizeIp:!0,cookieUpdate:!0,exFatal:!0,forceSSL:!0,javaEnabled:!0,legacyHistoryImport:!0,nonInteraction:!0,useAmpClientId:!0,useBeacon:!0,
storeGac:!0,allowAdFeatures:!0,allowAdPersonalizationSignals:!0,_cd2l:!0},y=function(N){var P=[].slice.call(arguments,0);P[0]=p+P[0];u.apply(window,P)},x=function(N,P){return void 0===P?P:N(P)},A=function(N,P){if(P)for(var Ba in P)P.hasOwnProperty(Ba)&&y("set",N+Ba,P[Ba])},B=function(){var N=function(Dn,Pj,En){if(!Ra(Pj))return!1;for(var id=Ha(Object(Pj),En,[]),pg=0;id&&pg<id.length;pg++)y(Dn,id[pg]);return!!id&&0<id.length},P;
if(e.vtp_useEcommerceDataLayer){var Ba=!1;Ba||(P=Vk("ecommerce",1))}else e.vtp_ecommerceMacroData&&(P=e.vtp_ecommerceMacroData.ecommerce);if(!Ra(P))return;P=Object(P);var db=Ha(h,"currencyCode",P.currencyCode);void 0!==db&&y("set","&cu",db);N("ec:addImpression",P,"impressions");if(N("ec:addPromo",P[P.promoClick?"promoClick":"promoView"],"promotions")&&
P.promoClick){y("ec:setAction","promo_click",P.promoClick.actionField);return}for(var za="detail checkout checkout_option click add remove purchase refund".split(" "),Va="refund purchase remove checkout checkout_option add click detail".split(" "),eb=0;eb<za.length;eb++){var nb=P[za[eb]];if(nb){N("ec:addProduct",nb,"products");y("ec:setAction",za[eb],nb.actionField);if(Od)for(var Db=0;Db<Va.length;Db++){var yc=P[Va[Db]];if(yc){yc!==nb&&D(13);break}}break}}},
z=function(N,P,Ba){var db=0;if(N)for(var za in N)if(N.hasOwnProperty(za)&&(Ba&&v[za]||!Ba&&void 0===v[za])){var Va=w[za]?Da(N[za]):N[za];"anonymizeIp"!=za||Va||(Va=void 0);P[za]=Va;db++}return db},E={name:t};e.vtp_transportUrl&&(h._x_19=e.vtp_transportUrl);z(h,E,!0);u("create",
e.vtp_trackingId||f.trackingId,E);y("set","&gtm",Fh(!0));Kc()&&y("set","&gcs",Sc());h._x_19&&(null==jc&&delete h._x_19,h._x_20&&!b[t]&&(b[t]=!0,u(ah(t,h._x_20))));e.vtp_enableRecaptcha&&y("require","recaptcha","recaptcha.js");(function(N,P){void 0!==e[P]&&y("set",N,e[P])})("nonInteraction","vtp_nonInteraction");A("contentGroup",
k);A("dimension",l);A("metric",m);var G={};z(h,G,!1)&&y("set",G);var L;e.vtp_enableLinkId&&y("require","linkid","linkid.js");y("set","hitCallback",function(){var N=h&&h.hitCallback;qa(N)&&N();e.vtp_gtmOnSuccess()});if("TRACK_EVENT"==e.vtp_trackType){e.vtp_enableEcommerce&&
(y("require","ec","ec.js"),B());var Q={hitType:"event",eventCategory:String(e.vtp_eventCategory||f.category),eventAction:String(e.vtp_eventAction||f.action),eventLabel:x(String,e.vtp_eventLabel||f.label),eventValue:x(Ca,e.vtp_eventValue||f.value)};z(L,Q,!1);y("send",Q);}else if("TRACK_SOCIAL"==e.vtp_trackType){var S={hitType:"social",socialNetwork:String(e.vtp_socialNetwork),
socialAction:String(e.vtp_socialAction),socialTarget:String(e.vtp_socialActionTarget)};z(L,S,!1);y("send",S);}else if("TRACK_TRANSACTION"==e.vtp_trackType){}else if("TRACK_TIMING"==e.vtp_trackType){}else if("DECORATE_LINK"==e.vtp_trackType){}else if("DECORATE_FORM"==e.vtp_trackType){}else if("TRACK_DATA"==e.vtp_trackType){}else{e.vtp_enableEcommerce&&(y("require","ec","ec.js"),B());if(e.vtp_doubleClick||"DISPLAY_FEATURES"==e.vtp_advertisingFeaturesType){var X="_dc_gtm_"+String(e.vtp_trackingId).replace(/[^A-Za-z0-9-]/g,"");y("require","displayfeatures",void 0,{cookieName:X})}if("DISPLAY_FEATURES_WITH_REMARKETING_LISTS"==e.vtp_advertisingFeaturesType){var xa="_dc_gtm_"+String(e.vtp_trackingId).replace(/[^A-Za-z0-9-]/g,
"");y("require","adfeatures",{cookieName:xa})}L?y("send","pageview",L):y("send","pageview");e.vtp_autoLinkDomains&&Yg(p,e.vtp_autoLinkDomains,!!e.vtp_useHashAutoLink,!!e.vtp_decorateFormsAutoLink);}if(!a){var na=e.vtp_useDebugVersion?"u/analytics_debug.js":"analytics.js";e.vtp_useInternalVersion&&!e.vtp_useDebugVersion&&(na="internal/"+na);a=!0;var cb=rh(h._x_19,"/analytics.js"),
la=cg("https:","http:","//www.google-analytics.com/"+na,h&&h.forceSSL);R("analytics.js"===na&&cb?cb:la,function(){var N=Vg();N&&N.loaded||e.vtp_gtmOnFailure();},e.vtp_gtmOnFailure)}}else I(e.vtp_gtmOnFailure)};Z.__ua=c;Z.__ua.b="ua";Z.__ua.g=!0;Z.__ua.priorityOverride=0}();
Z.a.uv=["google"],function(){(function(a){Z.__uv=a;Z.__uv.b="uv";Z.__uv.g=!0;Z.__uv.priorityOverride=0})(function(){})}();



Z.a.ytl=["google"],function(){function a(){var w=Math.round(1E9*Math.random())+"";return H.getElementById(w)?a():w}function b(w,y){if(!w)return!1;for(var x=0;x<u.length;x++)if(0<=w.indexOf("//"+u[x]+"/"+y))return!0;return!1}function c(w){var y=-1!==w.indexOf("?")?"&":"?";if(-1<w.indexOf("origin="))return w+y+"enablejsapi=1";if(!t){var x=U("document");t=x.location.protocol+"//"+x.location.hostname;x.location.port&&(t+=":"+x.location.port)}return w+y+"enablejsapi=1&origin="+encodeURIComponent(t)}function d(w,
y){var x=w.getAttribute("src");if(b(x,"embed/")){if(0<x.indexOf("enablejsapi=1"))return!0;if(y)return w.setAttribute("src",c(x)),!0}return!1}function e(w,y){if(!w.getAttribute("data-gtm-yt-inspected-"+y.vd)&&(w.setAttribute("data-gtm-yt-inspected-"+y.vd,"true"),d(w,y.we))){w.id||(w.id=a());var x=U("YT"),A=x.get(w.id);A||(A=new x.Player(w.id));var B=h(A,y),z={},E;for(E in B)z.Xa=E,B.hasOwnProperty(z.Xa)&&A.addEventListener(z.Xa,function(G){return function(L){return B[G.Xa](L.data)}}(z)),z={Xa:z.Xa}}}
function f(w){I(function(){function y(){for(var A=x.getElementsByTagName("iframe"),B=A.length,z=0;z<B;z++)e(A[z],w)}var x=U("document");y();vk(y)})}function h(w,y){var x,A;function B(){ca=Pk(function(){return{url:T,title:W,pe:J,pg:w.getCurrentTime(),playbackRate:X}},y.vd,w.getIframe());J=0;W=T="";X=1;return z}function z(la){switch(la){case p.PLAYING:J=Math.round(w.getDuration());T=w.getVideoUrl();if(w.getVideoData){var N=w.getVideoData();W=N?N.title:""}X=w.getPlaybackRate();y.jg?ca.Ub("start"):ca.Nc();
M=m(y.fh,y.eh,w.getDuration());return E(la);default:return z}}function E(){xa=w.getCurrentTime();na=(new Date).getTime();ca.nh();V();return G}function G(la){var N;switch(la){case p.ENDED:return Q(la);case p.PAUSED:N="pause";case p.BUFFERING:var P=w.getCurrentTime()-xa;N=1<Math.abs(((new Date).getTime()-na)/1E3*X-P)?"seek":N||"buffering";w.getCurrentTime()&&(y.ig?ca.Ub(N):ca.Nc());O();return L;case p.UNSTARTED:return B(la);default:return G}}function L(la){switch(la){case p.ENDED:return Q(la);case p.PLAYING:return E(la);
case p.UNSTARTED:return B(la);default:return L}}function Q(){for(;A;){var la=x;Qk(A);la()}y.hg&&ca.Ub("complete",1);return B(p.UNSTARTED)}function S(){}function O(){A&&(Qk(A),A=0,x=S)}function V(){if(M.length&&0!==X){var la=-1,N;do{N=M[0];if(N.Da>w.getDuration())return;la=(N.Da-w.getCurrentTime())/X;if(0>la&&(M.shift(),0===M.length))return}while(0>la);x=function(){A=0;x=S;0<M.length&&M[0].Da===N.Da&&(M.shift(),ca.Ub("progress",N.Oe,N.Ve));V()};A=Rk(x,1E3*la)}}var ca,M=[],J,T,W,X,xa,na,cb=B(p.UNSTARTED);
A=0;x=S;return{onStateChange:function(la){cb=cb(la)},onPlaybackRateChange:function(la){xa=w.getCurrentTime();na=(new Date).getTime();ca.Nc();X=la;O();V()}}}function k(w){for(var y=w.split(","),x=y.length,A=[],B=0;B<x;B++){var z=parseInt(y[B],10);isNaN(z)||100<z||0>z||A.push(z/100)}A.sort(function(E,G){return E-G});return A}function l(w){for(var y=w.split(","),x=y.length,A=[],B=0;B<x;B++){var z=parseInt(y[B],10);isNaN(z)||0>z||A.push(z)}A.sort(function(E,G){return E-G});return A}function m(w,y,x){var A=
w.map(function(E){return{Da:E,Ve:E,Oe:void 0}});if(!y.length)return A;var B=y.map(function(E){return{Da:E*x,Ve:void 0,Oe:E}});if(!A.length)return B;var z=A.concat(B);z.sort(function(E,G){return E.Da-G.Da});return z}function r(w){w.vtp_triggerStartOption?q(w):Hg(function(){q(w)})}function q(w){var y=!!w.vtp_captureStart,x=!!w.vtp_captureComplete,A=!!w.vtp_capturePause,B=k(w.vtp_progressThresholdsPercent+""),z=l(w.vtp_progressThresholdsTimeInSeconds+""),E=!!w.vtp_fixMissingApi;if(y||x||A||B.length||
z.length){var G={jg:y,hg:x,ig:A,eh:B,fh:z,we:E,vd:void 0===w.vtp_uniqueTriggerId?"":w.vtp_uniqueTriggerId},L=U("YT"),Q=function(){f(G)};I(w.vtp_gtmOnSuccess);if(L)L.ready&&L.ready(Q);else{var S=U("onYouTubeIframeAPIReady");Xk("onYouTubeIframeAPIReady",function(){S&&S();Q()});I(function(){for(var O=U("document"),V=O.getElementsByTagName("script"),ca=V.length,M=0;M<ca;M++){var J=V[M].getAttribute("src");if(b(J,"iframe_api")||b(J,"player_api"))return}for(var T=O.getElementsByTagName("iframe"),W=T.length,
X=0;X<W;X++)if(!v&&d(T[X],G.we)){R("https://www.youtube.com/iframe_api");v=!0;break}})}}else I(w.vtp_gtmOnSuccess)}var u=["www.youtube.com","www.youtube-nocookie.com"],p={UNSTARTED:-1,ENDED:0,PLAYING:1,PAUSED:2,BUFFERING:3,CUED:5},t,v=!1;Z.__ytl=r;Z.__ytl.b="ytl";Z.__ytl.g=!0;Z.__ytl.priorityOverride=0}();
Z.a.cid=["google"],function(){(function(a){Z.__cid=a;Z.__cid.b="cid";Z.__cid.g=!0;Z.__cid.priorityOverride=0})(function(){return md.s})}();

Z.a.gclidw=["google"],function(){var a=["aw","dc","gf","ha","gp"];(function(b){Z.__gclidw=b;Z.__gclidw.b="gclidw";Z.__gclidw.g=!0;Z.__gclidw.priorityOverride=100})(function(b){I(b.vtp_gtmOnSuccess);var c,d,e,f;b.vtp_enableCookieOverrides&&(e=b.vtp_cookiePrefix,c=b.vtp_path,d=b.vtp_domain,b.vtp_enableCookieFlagsFeature&&(f=b.vtp_cookieFlags));var h=null;b.vtp_enableCookieUpdateFeature&&(h=!0,void 0!==b.vtp_cookieUpdate&&(h=!!b.vtp_cookieUpdate));var k={prefix:e,path:c,domain:d,flags:f};b.vtp_enableCrossDomainFeature&&
(b.vtp_enableCrossDomain&&!1===b.vtp_acceptIncoming||(b.vtp_enableCrossDomain||sf())&&Kf(a,k));Hf(k);Mf(["aw","dc"],k);Vf(h,k);var l=e;if(b.vtp_enableCrossDomainFeature&&b.vtp_enableCrossDomain&&b.vtp_linkerDomains){var m=b.vtp_linkerDomains.toString().replace(/\s+/g,"").split(",");Lf(a,m,b.vtp_urlPosition,!!b.vtp_formDecoration,l)}var r=Vk(C.M);Hh(!1,void 0!=r&&!1!==r);b.vtp_enableUrlPassthroughFeature&&b.vtp_enableUrlPassthrough&&Of()})}();

Z.a.aev=["google"],function(){function a(p,t){var v=ce(p,"gtm");if(v)return v[t]}function b(p,t,v,w){w||(w="element");var y=p+"."+t,x;if(r.hasOwnProperty(y))x=r[y];else{var A=a(p,w);if(A&&(x=v(A),r[y]=x,q.push(y),35<q.length)){var B=q.shift();delete r[B]}}return x}function c(p,t,v){var w=a(p,u[t]);return void 0!==w?w:v}function d(p,t){if(!p)return!1;var v=e(Sk());sa(t)||(t=String(t||"").replace(/\s+/g,"").split(","));for(var w=[v],y=0;y<t.length;y++)if(t[y]instanceof RegExp){if(t[y].test(p))return!1}else{var x=
t[y];if(0!=x.length){if(0<=e(p).indexOf(x))return!1;w.push(e(x))}}return!Il(p,w)}function e(p){m.test(p)||(p="http://"+p);return ke(me(p),"HOST",!0)}function f(p,t,v){switch(p){case "SUBMIT_TEXT":return b(t,"FORM."+p,h,"formSubmitElement")||v;case "LENGTH":var w=b(t,"FORM."+p,k);return void 0===w?v:w;case "INTERACTED_FIELD_ID":return l(t,"id",v);case "INTERACTED_FIELD_NAME":return l(t,"name",v);case "INTERACTED_FIELD_TYPE":return l(t,"type",v);case "INTERACTED_FIELD_POSITION":var y=a(t,"interactedFormFieldPosition");
return void 0===y?v:y;case "INTERACT_SEQUENCE_NUMBER":var x=a(t,"interactSequenceNumber");return void 0===x?v:x;default:return v}}function h(p){switch(p.tagName.toLowerCase()){case "input":return sc(p,"value");case "button":return tc(p);default:return null}}function k(p){if("form"===p.tagName.toLowerCase()&&p.elements){for(var t=0,v=0;v<p.elements.length;v++)qk(p.elements[v])&&t++;return t}}function l(p,t,v){var w=a(p,"interactedFormField");return w&&sc(w,t)||v}var m=/^https?:\/\//i,r={},q=[],u={ATTRIBUTE:"elementAttribute",
CLASSES:"elementClasses",ELEMENT:"element",ID:"elementId",HISTORY_CHANGE_SOURCE:"historyChangeSource",HISTORY_NEW_STATE:"newHistoryState",HISTORY_NEW_URL_FRAGMENT:"newUrlFragment",HISTORY_OLD_STATE:"oldHistoryState",HISTORY_OLD_URL_FRAGMENT:"oldUrlFragment",TARGET:"elementTarget"};(function(p){Z.__aev=p;Z.__aev.b="aev";Z.__aev.g=!0;Z.__aev.priorityOverride=0})(function(p){var t=p.vtp_gtmEventId,v=p.vtp_defaultValue,w=p.vtp_varType;switch(w){case "TAG_NAME":var y=a(t,"element");return y&&y.tagName||
v;case "TEXT":return b(t,w,tc)||v;case "URL":var x;a:{var A=String(a(t,"elementUrl")||v||""),B=me(A),z=String(p.vtp_component||"URL");switch(z){case "URL":x=A;break a;case "IS_OUTBOUND":x=d(A,p.vtp_affiliatedDomains);break a;default:x=ke(B,z,p.vtp_stripWww,p.vtp_defaultPages,p.vtp_queryKey)}}return x;case "ATTRIBUTE":var E;if(void 0===p.vtp_attribute)E=c(t,w,v);else{var G=p.vtp_attribute,L=a(t,"element");E=L&&sc(L,G)||v||""}return E;case "MD":var Q=p.vtp_mdValue,S=b(t,"MD",Ck);return Q&&S?Fk(S,Q)||
v:S||v;case "FORM":return f(String(p.vtp_component||"SUBMIT_TEXT"),t,v);default:return c(t,w,v)}})}();
Z.a.gas=["google"],function(){(function(a){Z.__gas=a;Z.__gas.b="gas";Z.__gas.g=!0;Z.__gas.priorityOverride=0})(function(a){var b=n(a),c=b;c[Hb.Ha]=null;c[Hb.lf]=null;var d=b=c;d.vtp_fieldsToSet=d.vtp_fieldsToSet||[];var e=d.vtp_cookieDomain;void 0!==e&&(d.vtp_fieldsToSet.push({fieldName:"cookieDomain",value:e}),delete d.vtp_cookieDomain);return b})}();
Z.a.remm=["google"],function(){(function(a){Z.__remm=a;Z.__remm.b="remm";Z.__remm.g=!0;Z.__remm.priorityOverride=0})(function(a){for(var b=a.vtp_input,c=a.vtp_map||[],d=a.vtp_fullMatch,e=a.vtp_ignoreCase?"gi":"g",f=0;f<c.length;f++){var h=c[f].key||"";d&&(h="^"+h+"$");var k=new RegExp(h,e);if(k.test(b)){var l=c[f].value;a.vtp_replaceAfterMatch&&(l=String(b).replace(k,l));return l}}return a.vtp_defaultValue})}();
Z.a.smm=["google"],function(){(function(a){Z.__smm=a;Z.__smm.b="smm";Z.__smm.g=!0;Z.__smm.priorityOverride=0})(function(a){var b=a.vtp_input,c=Jl(a.vtp_map,"key","value")||{};return c.hasOwnProperty(b)?c[b]:a.vtp_defaultValue})}();



Z.a.paused=[],function(){(function(a){Z.__paused=a;Z.__paused.b="paused";Z.__paused.g=!0;Z.__paused.priorityOverride=0})(function(a){I(a.vtp_gtmOnFailure)})}();
Z.a.hid=["google"],function(){(function(a){Z.__hid=a;Z.__hid.b="hid";Z.__hid.g=!0;Z.__hid.priorityOverride=0})(function(){return gk.Kb})}();
Z.a.zone=[],function(){function a(q){for(var u=q.vtp_boundaries||[],p=0;p<u.length;p++)if(!u[p])return!1;return!0}function b(q){var u=md.s,p=u+":"+q.vtp_gtmTagId,t=Vk("gtm.uniqueEventId")||0,v=Ag(function(){return new h}),w=a(q),y=q.vtp_enableTypeRestrictions?q.vtp_whitelistedTypes.map(function(G){return G.typeId}):null;y=y&&La(y,f);if(v.registerZone(p,t,w,y))for(var x=q.vtp_childContainers.map(function(G){return G.publicId}),A=0;A<x.length;A++){var B=String(x[A]);if(v.registerChild(B,u,p)){var z=
0!==B.indexOf("GTM-");if(z){var E=function(G,L){Wk(arguments)};E("js",new Date);m?(E("config",B),l||bl(B,z)):(K.addTargetToGroup(B),gj({},B))}else bl(B,z)}}}var c={active:!1,isAllowed:function(){return!1},isWhitelisted:function(){return!1}},d={active:!0,isAllowed:function(){return!0},isWhitelisted:function(){return!0}},e={zone:!0,cn:!0,css:!0,ew:!0,eq:!0,ge:!0,gt:!0,lc:!0,le:!0,lt:!0,re:!0,sw:!0,um:!0},f={cl:["ecl"],ecl:["cl"],ehl:["hl"],hl:["ehl"]},h=function(){this.h={};this.i={}};h.prototype.checkState=
function(q,u){var p=this.h[q];if(!p)return d;var t=this.checkState(p.Me,u);if(!t.active)return c;for(var v=[],w=0;w<p.Bd.length;w++){var y=this.i[p.Bd[w]];y.vb(u)&&v.push(y)}if(!v.length)return c;var x=function(A,B){B=B||[];if(!(t.isAllowed||t.isWhitelisted)(A,B))return!1;for(var z=0;z<v.length;++z)if(v[z].isAllowed?v[z].isAllowed(A,B):v[z].isWhitelisted(A,B))return!0;return!1};return{active:!0,isAllowed:x,isWhitelisted:x}};h.prototype.unregisterChild=function(q){delete this.h[q]};h.prototype.registerZone=
function(q,u,p,t){var v=this.i[q];if(v)return v.o(u,p),!1;if(!p)return!1;this.i[q]=new k(u,t);return!0};h.prototype.registerChild=function(q,u,p){var t=this.h[q];if(!t&&K[q]||t&&t.Me!==u)return!1;if(t)return t.Bd.push(p),!1;this.h[q]={Me:u,Bd:[p]};return!0};var k=function(q,u){this.h=[{eventId:q,vb:!0}];this.i=null;if(u){this.i={};for(var p=0;p<u.length;p++)this.i[u[p]]=!0}};k.prototype.o=function(q,u){var p=this.h[this.h.length-1];q<=p.eventId||p.vb!=u&&this.h.push({eventId:q,vb:u})};k.prototype.vb=
function(q){if(!this.h||0==this.h.length)return!1;for(var u=this.h.length-1;0<=u;u--)if(this.h[u].eventId<=q)return this.h[u].vb;return!1};k.prototype.isAllowed=function(q,u){u=u||[];if(!this.i||e[q]||this.i[q])return!0;for(var p=0;p<u.length;++p)if(this.i[u[p]])return!0;return!1};k.prototype.isWhitelisted=k.prototype.isAllowed;var l=!1;var m=!0;
var r=function(q){b(q);I(q.vtp_gtmOnSuccess)};Z.__zone=r;Z.__zone.b="zone";Z.__zone.g=!0;Z.__zone.priorityOverride=0}();
Z.a.html=["customScripts"],function(){function a(d,e,f,h){return function(){try{if(0<e.length){var k=e.shift(),l=a(d,e,f,h);if("SCRIPT"==String(k.nodeName).toUpperCase()&&"text/gtmscript"==k.type){var m=H.createElement("script");m.async=!1;m.type="text/javascript";m.id=k.id;m.text=k.text||k.textContent||k.innerHTML||"";k.charset&&(m.charset=k.charset);var r=k.getAttribute("data-gtmsrc");r&&(m.src=r,lc(m,l));d.insertBefore(m,null);r||l()}else if(k.innerHTML&&0<=k.innerHTML.toLowerCase().indexOf("<script")){for(var q=
[];k.firstChild;)q.push(k.removeChild(k.firstChild));d.insertBefore(k,null);a(k,q,l,h)()}else d.insertBefore(k,null),l()}else f()}catch(u){I(h)}}}var c=function(d){if(H.body){var e=
d.vtp_gtmOnFailure,f=dl(d.vtp_html,d.vtp_gtmOnSuccess,e),h=f.Yc,k=f.D;if(d.vtp_useIframe){}else d.vtp_supportDocumentWrite?b(h,k,e):a(H.body,uc(h),k,e)()}else Rk(function(){c(d)},
200)};Z.__html=c;Z.__html.b="html";Z.__html.g=!0;Z.__html.priorityOverride=0}();

Z.a.dbg=["google"],function(){(function(a){Z.__dbg=a;Z.__dbg.b="dbg";Z.__dbg.g=!0;Z.__dbg.priorityOverride=0})(function(){return!1})}();




Z.a.lcl=[],function(){function a(){var c=U("document"),d=0,e=function(f){var h=f.target;if(h&&3!==f.which&&!(f.Lg||f.timeStamp&&f.timeStamp===d)){d=f.timeStamp;h=vc(h,["a","area"],100);if(!h)return f.returnValue;var k=f.defaultPrevented||!1===f.returnValue,l=nk("lcl",k?"nv.mwt":"mwt",0),m;m=k?nk("lcl","nv.ids",[]):nk("lcl","ids",[]);if(m.length){var r=jk(h,"gtm.linkClick",m);if(b(f,h,c)&&!k&&l&&h.href){var q=String(cl(h,"rel")||""),u=!!ua(q.split(" "),function(v){return"noreferrer"===v.toLowerCase()});
u&&D(36);var p=U((cl(h,"target")||"_self").substring(1)),t=!0;if(Wk(r,Zj(function(){var v;if(v=t&&p){var w;a:if(u){var y;try{y=new MouseEvent(f.type)}catch(x){if(!c.createEvent){w=!1;break a}y=c.createEvent("MouseEvents");y.initEvent(f.type,!0,!0)}y.Lg=!0;f.target.dispatchEvent(y);w=!0}else w=!1;v=!w}v&&(p.location.href=cl(h,"href"))}),l))t=!1;else return f.preventDefault&&f.preventDefault(),f.returnValue=!1}else Wk(r,function(){},l||2E3);return!0}}};qc(c,"click",e,!1);qc(c,"auxclick",e,!1)}function b(c,
d,e){if(2===c.which||c.ctrlKey||c.shiftKey||c.altKey||c.metaKey)return!1;var f=cl(d,"href"),h=f.indexOf("#"),k=cl(d,"target");if(k&&"_self"!==k&&"_parent"!==k&&"_top"!==k||0===h)return!1;if(0<h){var l=Uk(f),m=Uk(e.location);return l!==m}return!0}(function(c){Z.__lcl=c;Z.__lcl.b="lcl";Z.__lcl.g=!0;Z.__lcl.priorityOverride=0})(function(c){var d=void 0===c.vtp_waitForTags?!0:c.vtp_waitForTags,e=void 0===c.vtp_checkValidation?!0:c.vtp_checkValidation,f=Number(c.vtp_waitForTagsTimeout);if(!f||0>=f)f=2E3;
var h=c.vtp_uniqueTriggerId||"0";if(d){var k=function(m){return Math.max(f,m)};mk("lcl","mwt",k,0);e||mk("lcl","nv.mwt",k,0)}var l=function(m){m.push(h);return m};mk("lcl","ids",l,[]);e||mk("lcl","nv.ids",l,[]);$k("lcl")||(a(),al("lcl"));I(c.vtp_gtmOnSuccess)})}();


var An={};An.macro=function(a){if(gk.Lc.hasOwnProperty(a))return gk.Lc[a]},An.onHtmlSuccess=gk.oe(!0),An.onHtmlFailure=gk.oe(!1);An.dataLayer=Zd;An.callback=function(a){ud.hasOwnProperty(a)&&qa(ud[a])&&ud[a]();delete ud[a]};function Bn(){K[md.s]=An;Ja(vd,Z.a);zb=zb||gk;Ab=yg}
function Cn(){zc.gtm_3pds=!0;zc.gtag_cs_api=!0;K=F.google_tag_manager=F.google_tag_manager||{};if(K[md.s]){var a=K.zones;a&&a.unregisterChild(md.s);}else{for(var b=data.resource||{},c=b.macros||[],d=0;d<c.length;d++)sb.push(c[d]);for(var e=b.tags||[],f=0;f<e.length;f++)vb.push(e[f]);for(var h=b.predicates||[],k=0;k<h.length;k++)ub.push(h[k]);for(var l=b.rules||[],m=0;m<l.length;m++){for(var r=l[m],q={},u=0;u<r.length;u++)q[r[u][0]]=Array.prototype.slice.call(r[u],1);tb.push(q)}xb=Z;yb=Dl;Bn();fk();Cg=!1;Dg=0;if("interactive"==H.readyState&&!H.createEventObject||"complete"==H.readyState)Fg();
else{qc(H,"DOMContentLoaded",Fg);qc(H,"readystatechange",Fg);if(H.createEventObject&&H.documentElement.doScroll){var p=!0;try{p=!F.frameElement}catch(y){}p&&Gg()}qc(F,"load",Fg)}Aj=!1;"complete"===H.readyState?Cj():qc(F,"load",Cj);a:{if(!Od)break a;F.setInterval(Pd,
864E5);}sd=(new Date).getTime();}}
(function(a){a()})(Cn);

})()
