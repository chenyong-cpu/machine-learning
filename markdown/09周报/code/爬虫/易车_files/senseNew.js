//2020062911 启用js-sdk项目
var bitAdFrame = {
    $: function (id) {
        return document.getElementById(id)
    },
    tagArr: function (o, name) {
        return o.getElementsByTagName(name)
    },
    nameArr: function (name) {
        return document.getElementsByName(name)
    },
    att: function (o, name, fun) {
        return document.all ? o.attachEvent(name, fun) : o.addEventListener(name.substr(2), fun, false)
    },
    style: function (o) {
        return o.currentStyle || document.defaultView.getComputedStyle(o, null)
    },
    scroll: function (type) {
        return document.documentElement[type] || document.body[type]
    },
    client: function (type) {
        return document.documentElement[type] || document.body[type]
    },
    buildTag: function (id, tagName, arr, object) {
        var obj = document.createElement(tagName);
        if (id) {
            obj.id = id
        }
        if (arr) {
            for (i = 0; i < arr.length; i++) {
                obj.style[arr[i][0]] = arr[i][1]
            }
        }
        object.appendChild(obj)
    },
    buildHtml: function(con, close, clickurl, counturl) {
        var str = "";
        var col = close ? ('<div style="font-size:12px;cursor:pointer;" onclick="this.parentNode.style.display=\'none\'">关闭</div>') : "";
        if (con.type == "image") {
            str = '<a href="' + con.link + '" target="_blank"><img src="' + con.url + '" style="border:none; width:' + con.width + "px;height:" + con.height + 'px"/></a>'
        } else {
            str += '<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="' + con.width + '" height="' + con.height + '">';
            str += '  <param name="movie" value="' + con.url + '" />';
            str += '  <param name="quality" value="high" />';
            str += ' <param value="transparent" name="wmode"/>';
            str += '  <embed src="' + con.url + '" quality="high"  wmode="transparent" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="' + con.width + '" height="' + con.height + '"></embed>';
            str += "</object>"
        }
        if (clickurl && clickurl != "") {
            str += '<div style="margin: -' + con.height + "px 0px 0px; cursor: pointer; background-image: url(//d2.yiche.com/img/bg.gif); position: relative; width: " + con.width + "px; height: " + con.height + 'px; z-index: 10; left: 0px;" onclick="RedirectOnClick(\'' + clickurl + "','" + counturl + "',true,true);\"></div>"
        }
        str += col;
        return str
    },
    roll: function (id, top) {
        var obj = bitAdFrame.$(id);
        var space = top + bitAdFrame.scroll("scrollTop"),
            objTop = parseInt(bitAdFrame.style(obj).top),
            pro = this,
            a;
        if (objTop < space) {
            a = (space - objTop) * 0.01;
            obj.style.top = objTop + a * 20 + "px"
        } else {
            if (objTop > space) {
                a = (objTop - space) * 0.01;
                obj.style.top = objTop - a * 20 + "px"
            }
        }
        setTimeout(function () {
            pro.roll(id, top)
        }, 10)
    }
};

function RedirectOnClick(url, newurl, recHit, newWin) {
    if (newWin) {
        window.open(url)
    } else {
        window.location.href = url
    } if (recHit && newurl && newurl != "undefined") {
        SendToPage(newurl + "&r=" + Math.random())
    }
}
function SendToPage(url) {
    var SendPageImg = new Image();
    SendPageImg.src = url
}
function getAttr(obj, attrName) {
    var temp = obj.getAttribute(attrName);
    if (temp == null) {
        temp = obj.getAttribute("data-" + attrName)
    }
    return ((temp == null) ? "" : escape(temp))
}
function getIsAdType(obj) {
    var adType = getAttr(obj, "type");
    if (adType == "ad_play" || adType == "ad_play_id") {
        return true;
    }
    return false;
}

function getAdIsFired(obj) {
    var ret = getAttr(obj, "isRendered");
    return (ret == "1") ? true: false;
}
function setAdFired(obj) {
    if (obj) {
        obj.setAttribute("isRendered", "1");
    }
}


function getvalue(paras) {
    var url = location.href;
    if (url.indexOf("#") != -1) {
        url = url.substring(0, url.indexOf("#"))
    }
    var paraString = url.substring(url.indexOf("?") + 1, url.length).split("&");
    var paraObj = {};
    for (var i = 0; i < paraString.length; i++) {
        var j = paraString[i];
        if (j.indexOf("=") > 0) {
            paraObj[j.substring(0, j.indexOf("=")).toLowerCase()] = j.substring(j.indexOf("=") + 1, j.length)
        }
    }
    var returnTempValue = "";
    var returnValue = paraObj[paras.toLowerCase()];
    if (typeof (returnValue) == "undefined") {
        returnTempValue = ""
    } else {
        returnTempValue = returnValue
    } if (returnTempValue == "") {
        if (window.parent) {
            returnTempValue = getvalueParent(paras)
        }
    }
    return returnTempValue
}
function getvalueParent(paras) {
    if (typeof(window.parent.location.href) == "undefined") {
        return "";
    }
    var url = window.parent.location.href;
    if (url.indexOf("#") != -1) {
        url = url.substring(0, url.indexOf("#"))
    }
    var paraString = url.substring(url.indexOf("?") + 1, url.length).split("&");
    var paraObj = {};
    for (var i = 0; i < paraString.length; i++) {
        var j = paraString[i];
        if (j.indexOf("=") > 0) {
            paraObj[j.substring(0, j.indexOf("=")).toLowerCase()] = j.substring(j.indexOf("=") + 1, j.length)
        }
    }
    var returnTempValue = "";
    var returnValue = paraObj[paras.toLowerCase()];
    if (typeof (returnValue) == "undefined") {
        returnTempValue = ""
    } else {
        returnTempValue = returnValue
    }
    return returnTempValue
}
function showSrc(src) {
    var oHead = document.getElementsByTagName("HEAD").item(0);
    var oScript = document.createElement("script");
    oScript.type = "text/javascript";
    oScript.src = src;
    oHead.appendChild(oScript)
}

var popupdate_ad = {
    'div_08c16d93-8064-4683-846e-e18538824115': 1,
    'div_857e089d-178f-4b2c-bc15-3f281405b734': 1,
    'div_065b00bb-0496-41d7-bf69-9eba2909f840': 1,
    'div_f8f23b88-4456-4f89-8255-938d844998d2': 1,
    'div_939834e2-de44-438c-af3e-7ef2a25b0c9e': 1
};

var _PreviewParams = {
    getPlayTime: function() {
        var p = getvalue("adplay_time");
        return (p == null || p == "") ? "" : p;
    },
    getCityId: function() {
        var p =  getvalue("adplay_cityid");
        return (p == null || p == "") ? "" : p;
    },
    getCityName: function() {
        var p = getvalue("adplay_cityname");
        return (p == null || p == "") ? "" : p;
    },
    getKeyword: function() {
        var p = getvalue("adplay_keyword");
        return (p == null || p == "") ? "" : p;
    },
    getBrandId: function() {
        var p = getvalue("adplay_brandid");
        return (p == null || p == "") ? "" : p;
    },
    getModelId: function() {
        var p = getvalue("adplay_modelid");
        return (p == null || p == "") ? "" : p;
    },
    getSearch: function() {
        var p = getvalue("adplay_search");
        return (p == null || p == "") ? "" : p;
    },
    getDspId: function() {
        var p = getvalue("adplay_dspid");
        return (p == null || p == "") ? "" : p;
    },
    getToAdxSbox: function() {
        var p = getvalue("adplay_sbox");
        return (p == null || p == "") ? "" : p;
    },
    toKanli2017: function() {
        var p = getvalue("adplay_2017");
        return (p == null || p == "") ? false : true;
    },
    fetchByOne: function() {
        return true;
    }
}

function getLocationCityId() {
    if (typeof (bit_locationInfo) == "undefined") {
        try {

            var _aes_src = document.createElement("script");
            _aes_src.src = location.protocol + "//static1.bitautoimg.com/yc-common/js/cryptojs.min.js";
            document.getElementsByTagName("head")[0].appendChild(_aes_src);

            var _iplocation_url = location.protocol + "//newsapi.yiche.com/citybase/encryptSetCookie";
            var _iplocation_src = document.createElement("script");
            _iplocation_src.src = _iplocation_url
            document.getElementsByTagName("head")[0].appendChild(_iplocation_src)
        } catch(err){
            sspTrigger.fireErrMonitor("getLocationCityId-1=" + sspTrigger.getErrMsg(err));
        }
    }
    try {
        if (typeof (Bitauto) != "undefined" && typeof (Bitauto.location) != "undefined" && typeof (Bitauto.location.cityId) != "undefined") {
            return Bitauto.location.cityId + "";
        }
        if (typeof (bit_locationInfo) != "undefined") {
            try{// 解密
                if (!bit_locationInfo instanceof Object) {
                    bit_locationInfo = JSON.parse(Decrypt(bit_locationInfo))
                }
            }catch(e){
                console.log(e)
            }
            if (typeof (bit_locationInfo.cityId) != "undefined") {
                return bit_locationInfo.cityId + "";
            }
        }
    } catch(err) {
        sspTrigger.fireErrMonitor("getLocationCityId-2=" + sspTrigger.getErrMsg(err));
    }
    return "0";
}

var _sspTolerance={
};

if (typeof _senseNewLoadedIns == "undefined"){
    _senseNewLoadedIns = {}
}

// 页面刷新ID
if (typeof BitautoPageRefreshIdForAd == "undefined") {
    BitautoPageRefreshIdForAd = '';
    var charss = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
    var maxPos = charss.length;
    for (i = 0; i < 32; i++) {
        BitautoPageRefreshIdForAd += charss.charAt(Math.floor(Math.random() * maxPos));
    }
    BitautoPageRefreshIdForAd = BitautoPageRefreshIdForAd + (new Date()).getTime();
}

var sspUtil={
    getPageParam:function(){
        return BitautoPageRefreshIdForAd;
    },
    addLoadIns:function(pid){
        if (pid && pid != ""){
            _senseNewLoadedIns[pid] = 1;
        }
    },
    isLoadIns:function(pid){
        if (pid && pid != "" && !_senseNewLoadedIns[pid]){
            return true;
        }else{
            return false;
        }
    },
    getBrowser:function(){
        var oType = "";
        var __bitauto_Browser_isIE = window.ActiveXObject ? true : false;
        if(__bitauto_Browser_isIE || navigator.userAgent.indexOf("MSIE")!= -1){
            oType="IE";
        }else if(navigator.userAgent.indexOf("Firefox")!=-1){
            oType="FIREFOX";
        }else if(navigator.userAgent.indexOf("WebKit")!=-1 ){
            oType="CHROME";
        }
        return oType;
    },
    getPageCharset:function(){
        var charSet = "";
        var oType = this.getBrowser();
        switch(oType){
            case "IE":
                charSet = document.charset;
                break;
            case "FIREFOX":
                charSet = document.characterSet;
                break;
            case "CHROME":
                charSet = document.characterSet;
                break;
            default:
                break;
        }
        return charSet;
    },
    getCookie:function(cname){
        // 只提供获取cookie使用
        // not yiche site use LM
        var page = sspUtil.getPageParam();
        var domain = document.domain.split('.').slice(-2).join('.'); // level-one domain
        if (domain !== "yiche.com" && domain !== "bitauto.com"){
            cname = "LM" + cname;
        }

        var name = cname + "=";
        var ca = document.cookie.split(';');
        for(var i=0; i<ca.length; i++)
        {
            var c = sspTrigger.trim(ca[i]);
            var val = c.substring(name.length,c.length);
            if (c.indexOf(name)==0){
                return val + "&page=" + page;
            }
        }
        //generate new cookie
        var charss = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
        var maxPos = charss.length;
        var uid = '';
        for (i = 0; i < 32; i++) {
            uid += charss.charAt(Math.floor(Math.random() * maxPos));
        }
        document.cookie= cname + "=" +escape(uid) +  ";domain=" + domain + ";expires=Sun, 23-Dec-2025 08:13:02 GMT";
        return escape(uid) + "&page=" + page;
    },
    redirectUrl:function(url,newOpen){
        if (newOpen) {
            window.open(url)
        } else {
            window.location.href = url
        }
    },
};

var __ssp_sync_load_block_code = {
    "div_85982be8-807e-4c07-a1bb-168ef7b27267": 1,
    "div_45af7588-0d79-4edf-8388-7fa52f85bb80": 1,
    "div_699895bc-0c92-407f-b1e5-5b2811eb4aad": 1,
    "div_e4398407-2d4f-4dd8-bc79-b0d33e521bcc": 1,
};

var sspTrigger={
    loadAsyncScript: function(url) {
        try {
            var script = document.createElement("script");
            script.type = "text/javascript";
            script.src = url;
            script.setAttribute("async","async");
            document.body.appendChild(script);
        } catch(err){}
    },
    loadSyncScript: function(url) {
        try {
            var script = document.createElement("script");
            script.type = "text/javascript";
            script.src = url;
            document.body.appendChild(script);
        } catch(err){}
    },
    DocumentWriteScript: function(url) {
        try {
            document.write("<sc" + "ript src='" + url + "' ></sc" + "ript>");
        } catch(err){}
    },
    preLoadTolerance:function(){

        var pids = document.getElementsByTagName("ins");
        var toleranceServer=location.protocol + "//d2.yiche.com/zmaterial/";
        for(var i=0;i<pids.length;i++){
            if(getIsAdType(pids[i])){
                var tempPidStr = pids[i].getAttribute("id");
                tempPidStr = this.trim(tempPidStr).substr(4);
                var url = toleranceServer + "utf8_bid_" + tempPidStr + ".js";
                this.loadAsyncScript(url);
            }
        }
    },
    loadTolerance:function(){
        var pids = document.getElementsByTagName("ins");
        for(var i=0;i<pids.length;i++){
            var tempPidStr = pids[i].getAttribute("id");
            if(pids[i].getAttribute("isRendered") !== "1" && getIsAdType(pids[i]) && sspUtil.isLoadIns(tempPidStr)){

                tempPidStr = this.trim(tempPidStr).substr(4);
                tempPidStr = "p_" + tempPidStr;
                if(_sspTolerance[tempPidStr]){
                    //console.log( _sspTolerance[tempPidStr]["html"]);
                    pids[i].innerHTML = _sspTolerance[tempPidStr]["html"];
                    if(pids[i].getAttribute("width") && pids[i].getAttribute("height")){
                        pids[i].style.width = pids[i].getAttribute("width");
                        pids[i].style.height= pids[i].getAttribute("height");
                        pids[i].style.display="inline-block";
                    }
                    sspCallBackSenseNew.sendTracking(_sspTolerance[tempPidStr]["durl"]);
                    pids[i].setAttribute("isRendered","1");
                }else{
                    //console.log("Tolerance did not loaded for pid " + tempPidStr);
                }
            }
        }
    },
    requestAdxServer:function(url){
        var script = document.createElement("script");
        script.type = "text/javascript";
        script.src = url;
        script.setAttribute("id","sspsdk_dyna");
        script.setAttribute("referrerpolicy","no-referrer-when-downgrade");
        document.body.appendChild(script);
    },
    fireErrMonitor: function(err) {
        var url = location.protocol + "//adx.yiche.com/error/pc-wap?s=" + escape(err);
        console.log(url);
        return;
        this.loadAsyncScript(url);
    },
    init:function(){
        var eventHander = function(e){
            var elem = e.target;
            if(elem.tagName.toLowerCase() === 'script' && elem.getAttribute('id')==='sspsdk_dyna'){
                sspTrigger.loadTolerance();
            }
        }
        if(document.addEventListener){
            document.addEventListener("error",eventHander,true);
        }else{
            document.attachEvent("error",eventHander);
        }
    },
    ltrim :function(s){
        return s.replace(/(^\s*)/g, "");
    },
    rtrim: function(s){
        return s.replace(/(\s*$)/g, "");
    },
    trim: function(s){
        if (typeof(s) == "undefined" || s == null) {return "";}
        return s.replace(/(^\s*)|(\s*$)/g, "");
    },
    getUrlRelativePath: function(str) {
        try{
            if (location.href.indexOf(location.protocol+"//photo") != 0) {
                return "0";
            }
            var _url    = document.location.toString();
            var _arrUrl = _url.split("//");
            var _start  = _arrUrl[1].indexOf("/");
            var _relUrl = _arrUrl[1].substring(_start);
            if(_relUrl.indexOf("?") != -1){
                _relUrl = _relUrl.split("?")[0];
            }
            var _pathUrlArr = _relUrl.split("/");
            if (typeof (_pathUrlArr[1]) != "undefined" && _pathUrlArr[1] == str) {
                console.log(_pathUrlArr[2]);
                return _pathUrlArr[2];
            }
            return "0";
        }catch(err){
            return "0";
        }
    },
    getModelId: function(obj) {
        var _modelId = "0";
        _modelId = _PreviewParams.getModelId();
        if (_modelId == "") {
            if (typeof (CarCommonCSID) != "undefined") {
                _modelId = CarCommonCSID;
                // 多个车型时随机投
                var _modelIdArray = _modelId.toString().split(",");
                var len = _modelIdArray.length;
                if (len > 1){
                    var randNum =  Math.floor(Math.random()*len);
                    _modelId = _modelIdArray[randNum];
                }
            } else {
                _modelId = getAttr(obj, "adplay_brandid");
                if (_modelId.length != 4) {
                    _modelId = "0";
                }
            }
            if (_modelId == "0") {
                _modelId = this.getUrlRelativePath("serial");
            }
        }
        return _modelId;

    },
    getBrandId: function(obj) {
        var _brandId = "0";
        _brandId = _PreviewParams.getBrandId();
        if (_brandId == "") {
            if (typeof (CarCommonCBID) != "undefined") {
                _brandId = CarCommonCBID
            } else {
                _brandId = getAttr(obj, "adplay_brandid");
                if (_brandId.length != 5) {
                    _brandId = "0";
                }
            }
            if (_brandId == "0") {
                _brandId = this.getUrlRelativePath("brand");
            }
        }
        return _brandId;
    },
    getCityId: function() {
        var _cityId = "";
        _cityId = _PreviewParams.getCityId();
        if (_cityId == "" && location.href.indexOf(location.protocol+"//mai") == 0) {
            var p = getvalue("cityid");
            _cityId = (p == null || p == "") ? "" : p;
        }
        if (_cityId == "" && location.href.indexOf(location.protocol+"//dealer.m.yiche.com") == 0) {
            var x = location.href.split("/");
            if (typeof(x) != "undefined" && x.length > 3) {
                _cityId = x[3];
            }
        }
        if (_cityId == "" && typeof(BitautoCityIdForAd) != "undefined"){
            _cityId = BitautoCityIdForAd;
        }
        if (_cityId == "") {
            _cityId = getLocationCityId();
        }

        return _cityId;
    },
    getKeywordId: function() {
        var _keywordId = "";
        _keywordId = _PreviewParams.getKeyword();
        if (_keywordId == "") {
            if (typeof (CarCommonKeywordID) != "undefined") {
                _keywordId = CarCommonKeywordID
            }
        }
        return _keywordId;
    },
    getSearch: function() {
        var _search = "";
        _search = _PreviewParams.getSearch();
        if (_search == "") {
            if (typeof (BitautoSearchForAd) != "undefined") {
                _search = BitautoSearchForAd;
            }
            if (_search == "") {
                _search= "0"
            }
        }
        return _search;
    },
    getKeyword: function(obj) {
        var _keyword = "";
        _keyword = _PreviewParams.getKeyword();
        if (_keyword == "") {
            _keyword = getAttr(obj, "keyword");
            if ( _keyword == "" && location.href.indexOf(location.protocol+"//baa") == 0) {
                _keyword = getAttr(obj, "adplay_cityname");
                if(_keyword == "") {
                    _keyword = getAttr(obj, "adplay_brandname");
                }
            }
        }
        return _keyword;
    },
    getAdxServerUrl: function() {
        var adxServer= "https://ptyw.yiche.com/ssp/echo/v1.0/en";
        if (sspUtil.getBrowser() == "IE") {
            adxServer= "https://adx.bitauto.com/ssp/echo/v1.0/en";
        }
        var adxABServer="https://ab.yiche.com/ssp/echo/v1.0/en";
        var mToSbox = _PreviewParams.getToAdxSbox();
        if (mToSbox == "") {
            return adxServer;
        } else {
            return adxABServer;
        }
    },
    getTimesParam: function(p,sep,t) {
        var ret = "";
        var first = true
        for (var i = 0; i < t; i++) {
            if (first) {
                ret = p;
                first = false;
            } else {
                ret += sep + p;
            }
        }
        return ret;
    },
    fireOne: function(objDiv) {
        var requestUrl= "";
        var myCharset = sspUtil.getPageCharset();
        var myLocation = location.href;
        var myRandom = Math.floor(Math.random()*10000);


        var pidStr= "";
        var areaId = "0";
        var brandId = "0";
        var modelId = "0";
        var search = "0";
        var mKeywordIds = "";

        var myCookie = sspUtil.getCookie("CIGDCID");
        var mPlayTime = _PreviewParams.getPlayTime();
        var m = ",";

        if (areaId == "0" || areaId == "") {
            areaId = this.getCityId();
        }
        if (brandId == "0" || brandId == "") {
            brandId = this.getBrandId(objDiv);
        }
        if (modelId == "0" || modelId == "") {
            modelId = this.getModelId(objDiv);
        }
        if (mKeywordIds == "0" || mKeywordIds == "") {
            mKeywordIds = this.getKeywordId();
        }
        if (search == "0" || search == "") {
            search = this.getSearch();
        }

        var tempPidStr = objDiv.getAttribute("id");
        if (popupdate_ad[tempPidStr] == 1) {
            objDiv.setAttribute("id", "popupadcode");
        }
        if (tempPidStr.indexOf("_") > 0) {
            tempPidStr = this.trim(tempPidStr).substr(4);
        } else {
            this.fireErrMonitor("unknow-block-code=" + tempPidStr);
            tempPidStr = getAttr(objDiv, "adplay_BlockCode");
            objDiv.setAttribute("id", "div_" + tempPidStr);
        }
        pidStr = tempPidStr;
        requestUrl = this.getAdxServerUrl() + "?pid=" + pidStr;
        for(ins in wap_anti_ad_ins) {
            if(pidStr.indexOf(ins)<0) {
                requestUrl = requestUrl + "&" + "cs=" + myCharset;
            }
        }
        requestUrl = requestUrl + "&ord=" + myRandom + "&areaId="  + areaId + "&brandId=" + brandId + "&modelId=" + modelId
            + "&keywordId=" + mKeywordIds + "&search=" + search
            + "&CIGDCID=" + myCookie + "&callback=sspCallBackSenseNew.handleJson";
        if(mPlayTime != "") {
            requestUrl += "&date=" + mPlayTime;
        }
        this.requestAdxServer(requestUrl);

    },
    fire:function(){
        var requestUrl= "";
        var myCharset = sspUtil.getPageCharset();
        var myLocation = location.href;
        var myRandom = Math.floor(Math.random()*10000);


        var pidStr= "";
        var areaId = "";
        var brandId = "";
        var search = "";
        var modelId = "";
        var mKeywords = "";
        var mKeywordIds = ""

        var objdivs = document.getElementsByTagName("ins");
        var myCookie = sspUtil.getCookie("CIGDCID");
        var mPlayTime = _PreviewParams.getPlayTime();
        var m = ",";
        var reqUrlList = new Array();
        var arrLength = 0;
        var maxLengthIns = 10;
        var arrLengthIns = 0;

        var aCityId = "0";
        var aBrandId = "0";
        var aModelId = "0";
        var aKeywordId = "";
        var aKeyword = "";
        var aSearch = "0";

        for(var i=0;i<objdivs.length;i++){
            if (getIsAdType(objdivs[i])) {
                if (aCityId == "0" || aCityId == "") {
                    aCityId = this.getCityId();
                }
                if (aBrandId == "0" || aBrandId == "") {
                    aBrandId = this.getBrandId(objdivs[i]);
                }
                if (aModelId == "0" || aModelId == "") {
                    aModelId = this.getModelId(objdivs[i]);
                }
                if (aSearch == "0" || aSearch == "") {
                    aSearch = this.getSearch();
                }
            }
        }
        if (aKeywordId == "0" || aKeywordId == "") {
            aKeywordId = this.getKeywordId();
        }

        for(var i=0;i<objdivs.length;i++){
            var tempPidStr = objdivs[i].getAttribute("id");
            if (getIsAdType(objdivs[i]) && !getAdIsFired(objdivs[i]) && sspUtil.isLoadIns(tempPidStr)) {
                sspUtil.addLoadIns(tempPidStr);
                if (popupdate_ad[tempPidStr] == 1) {
                    objdivs[i].setAttribute("id", "popupadcode");
                }
                if (tempPidStr.indexOf("_") > 0) {
                    tempPidStr = this.trim(tempPidStr).substr(4);
                } else {
                    this.fireErrMonitor("unknow-block-code=" + tempPidStr);
                    tempPidStr = getAttr(objdivs[i], "adplay_BlockCode");
                    objdivs[i].setAttribute("id", "div_" + tempPidStr);
                }

                arrLengthIns += 1;
                if (arrLengthIns > maxLengthIns) {
                    arrLengthIns = 1;
                    arrLength++;
                    pidStr= "";
                    areaId = "";
                    brandId = "";
                    modelId = "";
                    mKeywordIds = "";
                    search = "";
                }

                if (arrLengthIns == 1) {
                    pidStr = tempPidStr;
                } else {
                    pidStr += m + tempPidStr;
                }
                areaId = this.getTimesParam(aCityId, m, arrLengthIns);
                brandId = this.getTimesParam(aBrandId, m, arrLengthIns);
                modelId = this.getTimesParam(aModelId, m, arrLengthIns);
                search = this.getTimesParam(aSearch, m , arrLengthIns);
                mKeywordIds = this.getTimesParam(aKeywordId, "||", arrLengthIns);
                requestUrl = this.getAdxServerUrl() + "?pid=" + pidStr;
                for(ins in wap_anti_ad_ins) {
                    if(pidStr.indexOf(ins)<0) {
                        requestUrl = requestUrl + "&" + "cs=" + myCharset;
                    }
                }
                if(pidStr.indexOf("d42d974e-6ddb-4b1f-845c-f0ab416e8e63")<0) {
                    requestUrl = requestUrl + "&" + "cs=" + myCharset;
                }

                requestUrl = requestUrl    + "&ord=" + myRandom + "&areaId="  + areaId + "&brandId=" + brandId + "&modelId=" + modelId
                    + "&keywordId=" + mKeywordIds + "&search=" + search
                    + "&CIGDCID=" + myCookie + "&callback=sspCallBackSenseNew.handleJson"
                if(mPlayTime != "") {
                    requestUrl += "&date=" + mPlayTime;
                }
                reqUrlList[arrLength] = requestUrl
            }
        }
        for (var i = 0; i < reqUrlList.length; i++) {
            if (this.IsSyncToCallAdx()) {
                this.DocumentWriteScript(reqUrlList[i]);
            } else {
                this.requestAdxServer(reqUrlList[i]);
            }
        }
    },
    IsSyncToCallAdx:function() {
        if (location.href.indexOf(location.protocol+"//baa") == 0 ||
            location.href.indexOf(location.protocol+"//m.yiche") == 0 ) {
            return true;
        }
        return false;
    },
    getErrMsg: function(err) {
        if (typeof(err) != "undefined") {
            return "err-type=" + err.name + ",err-msg=" + err.message;
        }
        return "";
    },
};

var ssp_hide_blockcode_ins = {
    "div_041222f6-5ef0-4c91-af71-102165f005b4": 1,
};

var wap_anti_ad_ins = [
    "d42d974e-6ddb-4b1f-845c-f0ab416e8e63",
    "c2d75cf6-24bf-46cf-858d-995e5804565e"
];

var ssp_ad_block_code_top_buttom = {
    "div_be5865ff-b854-438d-9863-d54af38d21a7": '1',
    "div_abe53914-1717-427b-9251-b207798ebdca": '1',
    "div_952ce0ee-507f-4f26-8f11-ce6c06812a49": '1',
    "div_569fe415-15f5-4ad2-9028-a49dce5186f9": '1',
    "div_94042601-39b4-4161-892a-b0608e589e6e": '1',
    "div_d3734235-3fbe-47fc-99ea-57669cedadf5": '1',
    "div_1a1c2052-cf6f-4a94-970c-f2a4847a3e80": '1',
    // "div_ea1bb82e-5ed2-4531-b960-8d354d3a011f": '1',
    "div_9ff50cb9-76d8-4054-9aec-c46d38c07ae2": '1',
    "div_fc718ffd-e00f-499c-be58-54f7dde02556": '1',
    "div_2bb1b2cb-71f3-40e6-9e0a-c041133c5bfe": '1',
    "buttom": '</ul></div></div></div></div></div>',
    "top": '<div class="ad-mt-20mb30"><div class="yiche-adv-type2 clearfix"><div class="col-auto left"><span class="title">车型推荐</span></div><div class="col-auto main"><div class="slide-box type-1 no-pager"><div class="slide-box-bg"><ul class="slide-box-big">',
};

var __ssptopbuttom1 = {
    "div_279a56d1-93e3-4cbb-9409-517fe7edec5a": '1',
    "div_c588f73d-9446-4cbb-a56f-941a8ddaa54f": '1',
    "div_0fdd1bab-745d-42d9-a86b-3dd5e25877b5": '1',
    "div_8a05b2f2-6da8-40a7-8296-d005d870b4bb": '1',
    "div_f53527fc-a2ff-4336-9d38-27a076a98cfb": '1',
    "div_f31814e7-225c-4e92-8ea9-c2876315cee0": '1',
    "div_2afe4673-39b3-4bad-9f48-38b0b6cb9513": '1',
    "div_20f3b410-22f8-4035-9bf7-3267a88bda6a": '1',
    "div_dbb76142-41ab-4a41-aa47-772616185c4b": '1',
    "top": '<div class="ad-line">',
    "buttom": '</div>',
};

var __ssptopbuttom2 = {
    "div_0c85cad5-bed4-4183-8ef1-2d76b85ac02e": '1',
    "div_48427d8f-eb70-4797-9717-4c806e2e6923": '1',
    "div_c9a71c91-999d-432a-bc96-591d3f37899e": '1',
    "div_d8210593-0930-4d3f-a776-259a9ef8c689": '1',
    "div_733322a8-ebf4-48ea-ad68-5c8fcf63c227": '1',
    "div_ffbfade2-2743-47c5-88c9-cf69e2c7f7a0": '1',
    "div_7fc82c82-6396-48b5-a021-2490ef193272": '1',
    "div_577f3fdf-82ed-4c49-8df6-8d4b90097ab8": '1',
    "div_3b060566-d15f-4790-893f-455069d72318": '1',
    "div_8bc7c932-302c-43a1-bd65-51c896f619c8": '1',
    "div_4acd9a92-158a-49ec-a0ad-989d9891b1e9": '1',
    "div_f983e9cb-d326-4cac-b85e-f8deb77a79f3": '1',
    "div_cfb83169-5c7f-48a8-99e6-34fc22a038fa": '1',
    "div_b7d7e3a6-62ff-4af1-b9e1-cc57c71d140a": '1',
    "div_3a4e2a73-d5f3-41b3-b59f-61370784bc9e": '1',
    "div_f49e86a6-5e55-4aed-a4c0-63545c5538b2": '1',
    "div_a2ce7d26-07a5-443a-854d-1e0f7f628950": '1',
    "div_536fb53c-6502-4a83-b561-64a0aea15992": '1',
    "div_29f1a813-03a6-4fdf-bb7d-7d229fcd7514": '1',
    "div_77933e35-c204-472b-b97c-4ac9866ea840": '1',
    "div_e47c8a3f-8123-42d6-b48c-2d8b2c7ec7df": '1',
    "div_fdb2befe-0828-4bc5-b663-0185ab6ef362": '1',
    "div_aedfa1f8-6a16-4a55-9a0e-8630637cfd79": '1',
    "div_a36f51c1-f885-440e-8b54-210eb2c9ed4d": '1',
    "div_cff3394c-ccaf-4910-9bef-b9602eb7e681": '1',
    "div_733322a8-ebf4-48ea-ad68-5c8fcf63c227": '1',
    "div_87d7bf9d-779d-4470-b61e-6e836b9a1bb5": '1',
    "div_1182e1fd-4f61-4046-b9b3-c87197b46a2a": '1',
    "div_72fbb147-4406-40e5-ba31-5576e1a04d5f": '1',
    "div_b7733dd1-6549-43b2-a3ae-e6b4ef4b20e7": '1',
    "div_b0563e06-ddf6-4450-8f79-70358624a7fc": '1',
    "div_b42dde88-244a-413b-8c89-7c0bd4f219f1": '1',
    "div_35784e83-511b-4601-9178-8df45638f930": '1',
    "div_2d0befcf-8490-45af-8fa8-dc3709405a68": '1',
    "div_0bbcf074-0e07-47c0-a7b1-d5c645fe69ac": '1',
    "div_20b7e84d-7a5d-461b-b484-b3d0fec5a81e": '1',
    "div_9e066309-54d0-4928-a251-b2f3c86ddc4d": '1',
    "div_8c25ad40-516a-4493-9ec6-6e0c3f499d58": '1',
    "div_9eb4c47a-ff47-4931-8f0f-598340ddaf23": '1',
    "div_50276862-a26d-4682-a49b-e143dac90475": '1',
    "div_6eda1bb3-a467-42a4-ba09-f4e683b2851d": '1',
    "top": '<div class="side-adv-box" style="margin:0 auto 10px">',
    "buttom": '</div>',
};

var __ssptopbuttom3 = {
    "div_cd11763a-ea3e-4315-b054-8baecd23cab8": '1',
    "div_893f9a91-0f1e-484c-8263-37d815e64d1b": '1',
    "div_09dc099f-5b52-4a70-8edd-faa0d7ff4818": '1',
    "div_469f45cc-1b72-461c-ba68-0b560c885455": '1',
    "div_9cab8046-e63a-435a-96ec-61213837984c": '1',
    "div_7729691d-e503-471d-8797-d0c5ea4978ab": '1',
    "div_5279e4d4-8875-4176-90eb-ca349a2392d5": '1',
    "top": '<div class="ad-txt-line"><em>广告</em>',
    "buttom": '</div>',
};

var ssp_m_car_blockcode_ins = {
    "div_19864": '1',
    "div_19863": '1',
    "div_19862": '1',
    "div_19861": '1',
    "div_19860": '1',
    "div_19867": '1',
    "div_19866": '1',
    "div_19865": '1'
};

var __IsCarStyleShufflingBlockCodeMap = {
    "ea1bb82e-5ed2-4531-b960-8d354d3a011f": '1',
    "div_ea1bb82e-5ed2-4531-b960-8d354d3a011f": '1',
    "div_18283": '1',
    "div_18284": '1',
    "div_18285": '1',
    "952ce0ee-507f-4f26-8f11-ce6c06812a49": '1',
    "div_952ce0ee-507f-4f26-8f11-ce6c06812a49": '1',
    "div_18348": '1',
    "div_18347": '1',
    "div_18346": '1',
    "be5865ff-b854-438d-9863-d54af38d21a7": '1',
    "div_be5865ff-b854-438d-9863-d54af38d21a7": '1',
    "div_18352": '1',
    "div_18353": '1',
    "div_18354": '1',
    "1a1c2052-cf6f-4a94-970c-f2a4847a3e80": '1',
    "div_1a1c2052-cf6f-4a94-970c-f2a4847a3e80": '1',
    "div_18341": '1',
    "div_18342": '1',
    "div_18340": '1',
    "div_abe53914-1717-427b-9251-b207798ebdca": '1',
    "abe53914-1717-427b-9251-b207798ebdca": '1',
    "div_18349": '1',
    "div_18351": '1',
    "div_18350": '1',
    "div_569fe415-15f5-4ad2-9028-a49dce5186f9": '1',
    "569fe415-15f5-4ad2-9028-a49dce5186f9": '1',
    "div_18357": '1',
    "div_18356": '1',
    "div_18355": '1',
    "div_94042601-39b4-4161-892a-b0608e589e6e": '1',
    "94042601-39b4-4161-892a-b0608e589e6e": '1',
    "div_18343": '1',
    "div_18345": '1',
    "div_18344": '1',
    "div_d3734235-3fbe-47fc-99ea-57669cedadf5": '1',
    "d3734235-3fbe-47fc-99ea-57669cedadf5": '1',
    "div_18360": '1',
    "div_18359": '1',
    "div_18358": '1',
    "div_1a1c2052-cf6f-4a94-970c-f2a4847a3e80": '1',
    "1a1c2052-cf6f-4a94-970c-f2a4847a3e80": '1',
    "div_18342": '1',
    "div_18341": '1',
    "div_18340": '1',
    "div_fc718ffd-e00f-499c-be58-54f7dde02556": '1',
    "fc718ffd-e00f-499c-be58-54f7dde02556": '1',
    "div_18280": '1',
    "div_18282": '1',
    "div_18281": '1',
    "div_2bb1b2cb-71f3-40e6-9e0a-c041133c5bfe": '1',
    "2bb1b2cb-71f3-40e6-9e0a-c041133c5bfe": '1',
    "div_18365": '1',
    "div_18364": '1',
    "div_18366": '1',
    "div_28062": '1',
    "div_28061": '1',
    "div_28060": '1',
    "div_9ff50cb9-76d8-4054-9aec-c46d38c07ae2": '1',
    "9ff50cb9-76d8-4054-9aec-c46d38c07ae2": '1',
    "top": '<div class="ad-mt-20mb30" style="display:none"><div class="yiche-adv-type2 clearfix"><div class="col-auto left"><span class="title">车型推荐</span></div><div class="col-auto main"><div class="slide-box type-1 no-pager"><div class="slide-box-bg"><ul class="slide-box-big">',
    "buttom": '</ul></div></div></div></div></div>',
};

var __IsAddJsByBlocks = {
    //"div_b2827653-8be0-406d-ba34-f13dbbd17f4d": '1'
    "div_b2827653-8be0-406d-ba34-f13dbbd17f4d": '1',
    "div_c62213b4-2900-4ed8-967d-3f3866014dc5": '1',
};


var sspCallBackSenseNew={

    sendTracking:function(url){
        try {
            var script = document.createElement("img");
            script.src     = url;
            script.width   = 0;
            script.height  = 0;
            script.style.display = "none";
            document.body.appendChild(script);
        } catch (err) {}
    },

    fireErrMonitor: function(err) {
        var url = location.protocol + "//adx.yiche.com/error/pc-wap?s=" + escape(err);
        console.log(url);
        return;
        this.loadAsyncScript(url);
    },

    handleJson:function(result){

        for(var i=0;i<result.length;i++){
            //console.log(result[i]);
            if(typeof(result[i].html) !== 'undefined' && result[i].html !=="" && result[i].html !== null){
                var insID = "div_" + result[i].ins;
                var isDisplay = true;
                var insInstance;
                if (popupdate_ad[insID] == 1) {
                    insInstance = document.getElementById("popupadcode");
                    isDisplay = false;
                } else {
                    insInstance = document.getElementById(insID);
                    if (typeof(insInstance) == 'undefined' || insInstance == null) {
                        insInstance = document.getElementById(" " + insID);
                    }
                    if (typeof(insInstance) == 'undefined' || insInstance == null) {
                        insInstance = document.getElementById(insID + " ");
                    }
                    if (typeof(insInstance) == 'undefined' || insInstance == null) {
                        continue;
                    }
                }
                if (ssp_hide_blockcode_ins[insID] == 1) {
                    isDisplay = false;
                }

                try {
                    if (__IsCarStyleShufflingBlockCodeMap[insID] == '1') {
                        var insInstanceParent = insInstance.parentNode;
                        var insInstanceParentInnerHtml = insInstanceParent.innerHTML + "" + result[i].html;
                        insInstanceParent.innerHTML = insInstanceParentInnerHtml;

                        var _CarStyleArr =document.getElementsByClassName("ad-mt-20mb30");
                        if (_CarStyleArr.length > 0) {
                            _CarStyleArr[0].style.display = "block";
                            var _slide_js = document.createElement("script");
                            _slide_js.src = "https://img1.bitautoimg.com/uimg/2016/yiche/js/adv-init.js";
                            document.getElementsByTagName("body")[0].appendChild(_slide_js);
                        }
                    } else if (ssp_ad_block_code_top_buttom[insID] == '1') {
                        insInstance.innerHTML = ssp_ad_block_code_top_buttom['top'] + result[i].html + ssp_ad_block_code_top_buttom['buttom'];
                    } else if (__ssptopbuttom1[insID] == '1') {
                        insInstance.innerHTML = __ssptopbuttom1['top'] + result[i].html + __ssptopbuttom1['buttom'];
                    } else if (__ssptopbuttom2[insID] == '1') {
                        insInstance.innerHTML = __ssptopbuttom2['top'] + result[i].html + __ssptopbuttom2['buttom'];
                    } else if (__ssptopbuttom3[insID] == '1') {
                        insInstance.innerHTML = __ssptopbuttom3['top'] + result[i].html + __ssptopbuttom3['buttom'];
                    } else {
                        insInstance.innerHTML = result[i].html;
                    }

                    setAdFired(insInstance);
                    if (isDisplay && insInstance.parentNode != null && insInstance.parentNode.style.display == "none" && !insInstance.getAttribute("isignoreparent")=="1" ) {
                        insInstance.parentNode.style.display = "block";
                    }
                    if (!isDisplay && insInstance.parentNode != null) {
                        insInstance.parentNode.style.display = "none";
                    }
                    for(var j=0;j<result[i].durl.length;j++){
                        this.sendTracking(result[i].durl[j]);
                    }
                } catch(err) {
                    this.fireErrMonitor("load-html-err-1"+ sspTrigger.getErrMsg(err));
                }

                // senseNew支持js渲染
                if(typeof(result[i].js) !== 'undefined' && result[i].js !=="" && result[i].js !== null){
                    //if (__IsAddJsByBlocks[insID] == '1') {
                    var script = document.createElement("script");
                    script.type = "text/javascript";
                    if(result[i].js.indexOf("try") > -1){
                        script.innerHTML = result[i].js;
                        document.body.appendChild(script);
                    } else {
                        script.innerHTML = "try{" + result[i].js + "}catch(err){}";
                        document.body.appendChild(script);
                    }
                    // }
                }

                if (typeof(result[i].ins) !== 'undefined' &&
                    typeof(ssp_m_car_blockcode_ins[insID]) !== 'undefined' && ssp_m_car_blockcode_ins[insID] == '1'){
                    try {
                        if(typeof adCallback == "function"){
                            adCallback(insID);
                        }
                    } catch(err){
                        this.fireErrMonitor("load-js-err-1"+ sspTrigger.getErrMsg(err));
                    }
                }
            }
        }
        var objects = document.getElementsByTagName('object');
        for (var i=0, m = objects.length; i < m; i++) { objects[i].style.display="block"; }
        var embeds = document.getElementsByTagName('embed');
        for (var i=0, m = embeds.length; i < m; i++) { embeds[i].style.display="block"; }
        if (location.href.indexOf("/cheshi/") > 0) {
            var reco1 = document.getElementById('recommendAdvDiv1');
            var reco2 = document.getElementById('recommendAdvDiv2');
            if (typeof(reco1) != "undefined" && reco1 != null) {
                reco1.style.display = 'none';
            }
            if (typeof(reco2) != "undefined" && reco2 != null) {
                reco2.style.display = 'none';
            }
            if (typeof (commonListObject) != "undefined") {
                commonListObject.InitTopLineLink();
                commonListObject.InitTopRatedLink();
                commonListObject.InitRecommendNewsPart();
            }
            var item = document.getElementById('divTopLineLink');
            if (item) {
                item.style.display = 'none';
            }

        }
    },
};

var YC_ADBLOCK_MAP = {"div_f3c1c3d0-46a4-4044-b536-43f702cd856a": [29447, 29448, 29445, 29446],
    "div_ea74f753-afad-4c67-a87c-d968cee67cf3": [26740, 26739, 26743, 26738, 26742, 26737, 26741],
    "div_9ff50cb9-76d8-4054-9aec-c46d38c07ae2": [28062, 28061, 28060, 18366, 18365, 18364],
    "div_307612a7-cb44-41d9-a3ff-13073ede5bef": [29603, 29608, 29599, 29604, 29600, 29605, 29601, 29606, 29602, 29607],
    "div_d23d3a98-cb1c-4573-931e-861f11449bc8": [29473, 24342, 29474],
    "div_b7047267-28f3-4d9c-a924-f70f51f08319": [18204, 18203, 18202],
    "div_be5865ff-b854-438d-9863-d54af38d21a7": [18354, 18353, 18352],
    "div_8d5a5746-62cf-4093-8b24-efa5f9dacffb": [28830, 28851, 28831, 28765, 28854, 28832, 28828, 28853, 28829, 28852],
    "div_192bdd20-adb3-40bb-8ffa-d739b40b4610": [27785, 27733, 27694, 27734, 27769, 27735, 27746, 27736, 27732],
    "div_5df98747-7530-43a4-b5df-f4eff6935ce6": [29579, 29575, 29576, 29577, 29574, 29578],
    "div_31913e2d-d152-4ea6-9547-fdbf589eca32": [27784, 27723, 27693, 27724, 27768, 27725, 27745, 27726, 27722],
    "div_a8b36ec5-900d-4865-b7be-d18917c4dc8b": [28602, 28643, 28644, 28645, 28601],
    "div_a33d3652-dc33-4a59-a5d0-5d68c60a2065": [27708, 27689, 27709, 27764, 27710, 27761, 27711, 27707, 27780],
    "div_df3be47b-9958-4a14-844f-f4818fb3c33a": [28957, 28958, 28959, 28960],
    "div_a19da821-fe0d-43a0-88d4-47953ddd8dc0": [24336, 24337, 24333, 24338, 24334, 24339, 24335],
    "div_8ecd70c8-5e23-4752-ae4b-fe63915952d4": [26125, 26120, 26124, 26121],
    "div_4f35128a-db6a-41f0-8e67-883fe9852115": [19782, 19760, 19761, 19762],
    "div_beb5192d-4722-4126-811b-ea10ae4c9663": [25146, 25145, 25190, 25189, 25188],
    "div_0f5cbb96-1858-410e-a68d-ea639f81b2d8": [18846, 18843, 18844, 18845],
    "div_06bfb1ae-1345-4398-8636-0fefacb57a4d": [28283, 28284, 28234, 28281, 28282],
    "div_98f50e33-b76f-4670-b9a9-33afa13e0b6d": [27713, 27690, 27714, 27765, 27715, 27744, 27716, 27712, 27781],
    "div_abdceb3d-7042-4fc0-8141-f0f7371e966d": [27747, 27586, 27588, 27587, 27583, 27774, 27584, 27748, 27585],
    "div_82cde721-4780-4526-9b56-b3a5d7837199": [28969, 28970, 28971],
    "div_c0fa081e-b0b0-40a7-8deb-ca4c30fb6b13": [29147, 29148, 29149, 29145, 29150, 29146],
    "div_94dd512f-caeb-4d8d-b910-6cc4fb18c21c": [24492, 25029, 24487, 25024, 24496, 24482, 24491, 25028, 24486, 24495, 25032, 24490, 25027, 24499, 24485, 24494, 25031, 24489, 25026, 24498, 24484, 24493, 25030, 24488, 25025, 24497, 24483],
    "div_1385c5c5-0f3c-4722-91e4-8c93d76aeaa7": [29664, 29665, 29666, 29662, 29667, 29663],
    "div_e4401f26-59c6-46ee-854a-34d68a3d1c3a": [29213, 29214, 29210, 29215, 29211, 29212],
    "div_b274c878-dca6-4e8a-9fcc-4e061baca9b1": [29685, 29690, 29686, 29691, 29687, 29692, 29683, 29688, 29693, 29684, 29689],
    "div_5fdbd3d8-cd0f-4470-93d0-abe04def89bd": [29443, 29444, 29441, 29442],
    "div_c4715026-5ea5-4802-b6b2-348c6744c2cc": [28611, 28612, 28608, 28609, 28610],
    "div_3e3470e2-eee4-4461-89f6-c5c8519d2961": [25980, 25979, 25978, 25982, 25977, 25981],
    "div_922360ca-8333-47ec-90db-23495854e782": [29506, 29507],
    "div_287f1f18-223a-4839-b8be-13fea8afd6df": [27625, 27612, 27608, 27777, 27609, 27756, 27610, 27755, 27611],
    "div_322e7101-4aed-4802-a59f-773574d59ff9": [29659, 29660, 29676, 29661, 29657, 29658],
    "div_80a90cb2-c14a-4d46-abf1-a9726ae07b3b": [19555, 19556, 19557],
    "div_7b378267-0135-4773-b2b6-f88fe7497a66": [29347, 29346],
    "div_0f3aea6c-b429-463c-95e4-c79106ac85a7": [25264, 25263, 25262, 25261, 25265, 25260],
    "div_b5877019-42c3-4280-acb5-e45d92c20896": [27990, 28020, 27986, 28016, 27991, 28021, 27987, 28017, 27992, 28022, 27988, 28018, 27993, 27984, 28023, 27989, 28019, 27985, 28024, 28015],
    "div_e3a8c38b-4e29-4fed-ae2f-d73076996be8": [29098, 29103, 29099, 29100, 29101, 29102],
    "div_1a1c2052-cf6f-4a94-970c-f2a4847a3e80": [18342, 18341, 18340],
    "div_8226f760-6d34-42e5-90df-0438836ff966": [17250, 17249, 17248],
    "div_c097f345-b3e7-4703-a370-64087699e3fe": [18842, 18839, 18840, 18841],
    "div_322049b4-9573-40df-8201-2669baa1d3d4": [29409, 29410, 29411, 29412],
    "div_b082c925-ba54-4906-a38c-2792dd3941db": [28859, 28855, 28860, 28654, 28856, 28655, 28857, 28656, 28858, 28657],
    "div_17a2fc9d-0f76-46a8-b8f3-d54b277a0af9": [29198, 29203, 29199, 29200, 29201, 29202],
    "div_dcad4689-f668-4599-9ad7-c9754f18e066": [19786, 19787, 19788, 19785],
    "div_cf8d4eea-bc64-4312-87cd-e94f236bc776": [27605, 27753, 27606, 27624, 27752, 27607, 27603, 27604, 27776],
    "div_ff4e968e-4da8-43b2-b186-f168f01604d1": [24343, 29472, 26855],
    "div_ad5c215e-4b8f-4d89-b211-d030563fddae": [29119, 29110, 29124, 29115, 29120, 29111, 29125, 29116, 29121, 29112, 29126, 29117, 29122, 29113, 29127, 29118, 29123, 29114],
    "div_034e2236-8e22-4700-98c9-a8602bede28e": [29569, 29565, 29570, 29561, 29566, 29571, 29562, 29567, 29563, 29568, 29564],
    "div_569fe415-15f5-4ad2-9028-a49dce5186f9": [18357, 18356, 18355],
    "div_008e50d8-27ab-4256-ad63-1f7ec115c093": [29170, 29168, 29172],
    "div_d6fd53eb-40e5-40d9-b6e1-e7b1ee29463f": [29862, 29863, 29864, 29861],
    "div_6cd24bed-3698-4ccf-b0e8-03c53d4ee36f": [19776, 19781, 19770, 19777, 19771, 19778, 19774, 19772, 19779, 19775, 19773, 19780],
    "div_7ccb0b46-aac2-4aff-8498-bcc5742e128e": [29637, 29638, 29639],
    "div_4879c233-2f78-40b0-b6bf-9513fa32ba1a": [28289, 28285, 28286, 28287, 28288],
    "div_66b96ed5-c06d-4c18-ae3b-b64fd3c2a1d3": [29106, 29107, 29108, 29104, 29109, 29105],
    "div_40fd2546-a7aa-40c2-967c-68cd3204c5d9": [29169, 29171, 29173],
    "div_9a0788f7-a67a-4585-8ce7-c7ef7db45809": [29855, 29856, 29865, 29866],
    "div_b6145660-2850-4e14-9ae4-9b1df8f9b7a1": [30074, 30081],
    "div_2e81691b-7b3d-45a9-b909-3084b41369e6": [28875, 28871, 28876, 28872, 28873, 28874],
    "div_eb08a641-3b9a-421f-ba15-7c447dc71db7": [28968, 28966, 28967],
    "div_1eacad6f-fd73-4477-998a-b16a5e0ced92": [26850, 24341, 27271],
    "div_a5d5688f-0070-4014-a4c0-cf8c9db42daf": [25577, 24347, 27552],
    "div_86346b52-b822-4bc8-9737-f70bf6ffdb7f": [28662, 28663, 28660, 28661],
    "div_2d584bc5-283d-4902-a717-dd46f5660a86": [29218, 29217, 29216],
    "div_307808ae-1e36-4641-b39d-7db77bc8bd02": [29236, 29194, 29195, 29196, 29197, 29304],
    "div_13c70d37-4825-433e-a2bb-648fbe8234ca": [29221, 29226, 29222, 29223, 29224, 29225],
    "div_72c2d3ef-3d63-45b1-b4fa-03a702a6f774": [28482, 28483],
    "div_7b01acbf-1c04-40f0-892a-36ddc880eef3": [24427, 24426, 24425],
    "div_d936dd7c-6c4e-438a-ab60-8b4b5df37280": [27779, 27620, 27760, 27621, 27743, 27627, 27622, 27618, 27619],
    "div_e52069d8-078e-42c6-ba02-aee3c58a9d92": [27949, 27963, 27954, 27945, 27959, 27950, 27955, 27946, 27960, 27951, 27956, 27947, 27961, 27952, 27957, 27948, 27962, 27953, 27944, 27958],
    "div_b5e9d63c-1b26-4a76-972a-70aa80eef925": [24414, 24418, 24417, 24416, 24415, 24419],
    "div_fc718ffd-e00f-499c-be58-54f7dde02556": [18280, 18282, 18281],
    "div_9e9e5fa2-e0fe-4bf4-9162-d3915be56b2e": [19804, 19803],
    "div_d7c0706e-8cb9-4b98-81af-00e922c3ef61": [17251, 17253, 17252],
    "div_1a726617-3821-46b1-89cb-1f49d68d7766": [18204, 18202, 18203],
    "div_0262b3cd-eb4f-4b4f-9901-ca494d2dc579": [29207, 29208, 29204, 29209, 29205, 29206],
    "div_19b0a5f4-6cc0-409f-9973-70c94bb72c9c": [17581, 17401],
    "div_4b4d0964-ad30-44c4-bf4c-9a0bbceef224": [27697, 27698, 27699, 27695, 27773, 27696],
    "div_86bd7ec1-5b2a-46b6-9852-8370113a3b1a": [28037, 27521, 24346],
    "div_9c030e70-d1f0-498a-9f9b-d97a9f792b58": [24421, 24420, 24424, 24423, 24422],
    "div_94042601-39b4-4161-892a-b0608e589e6e": [18343, 18345, 18344],
    "div_b5873cd5-dfd3-4da0-b449-e9f27acd71de": [19791, 19792, 19789, 19790],
    "div_6d0f7b40-9f73-4918-8c9f-28362d2b5c0a": [24345, 25153, 25120],
    "div_f71671d2-27d9-44f9-8347-226d3cdcd9be": [19814, 19811, 19812, 19813],
    "div_a65be867-de46-498b-89d3-9433e72104ed": [29136, 29303, 29141, 29132, 29137, 29133, 29138, 29134, 29139, 29135, 29140, 29165],
    "div_63987943-c025-45a3-b575-33de8440b15c": [25340, 25335, 25344, 25339, 25343, 25338, 25342, 25337, 25341, 25336],
    "div_8ab1eccb-c76b-4473-b4fd-091a25f2bd2c": [28763, 28762, 28761, 28836, 28760, 28837],
    "div_a2c842c5-c353-488d-8176-7bd2c07071a3": [28667, 28664, 28665, 28666],
    "div_46059978-7741-4188-af5c-ea416e476c27": [28756, 28633, 28637, 28755, 28634, 28754, 28635, 28758, 28636, 28757],
    "div_878f6684-120b-4149-b440-eaf03636966a": [29187, 29178, 29183, 29174, 29188, 29179, 29184, 29175, 29189, 29180, 29185, 29176, 29190, 29181, 29186, 29177, 29191, 29182],
    "div_abe53914-1717-427b-9251-b207798ebdca": [18349, 18351, 18350],
    "div_6de23012-6ce2-44bd-9b1c-75afa463ded5": [27654, 27652, 27648, 27649, 27650, 27651],
    "div_18bfbfa7-8e57-470b-96b1-5b8441b57761": [19742, 19743, 19739, 19744, 19740, 19741],
    "div_72ab8d0e-657a-4b6c-8c48-b9c817f0f4eb": [27595, 27596, 27771, 27597, 27593, 27594],
    "div_eeb5d275-7e82-4264-98cd-fdbb47e56b92": [27981, 27972, 27977, 27968, 27982, 27973, 27964, 27978, 27969, 27983, 27974, 27965, 27979, 27970, 27975, 27966, 27980, 27971, 27976, 27967],
    "div_952ce0ee-507f-4f26-8f11-ce6c06812a49": [18348, 18347, 18346],
    "div_f1d3c870-577e-4878-bdae-0dd1e11d5480": [27884, 27848, 27875, 27839, 27889, 27574, 27853, 27880, 27770, 27844, 27835, 27885, 27849, 27876, 27840, 27890, 27575, 27881, 27845, 27836, 27886, 27571, 27850, 27877, 27841, 27891, 27882, 27846, 27873, 27837, 27887, 27572, 27851, 27878, 27842, 27892, 27883, 27847, 27874, 27838, 27888, 27573, 27852, 27879, 27843, 27834],
    "div_d5ab1543-0681-437e-acf1-bf2c9adc659b": [27599, 27775, 27600, 27750, 27601, 27623, 27741, 27602, 27598],
    "div_1ac7dbbb-fcea-4493-b937-10c0601050b1": [29621, 29626, 29631, 29622, 29627, 29623, 29628, 29624, 29629, 29625, 29630],
    "div_88c0f8ff-6dc5-4fbd-9e87-4a0d0d36564b": [19795, 19796, 19793, 19794],
    "div_e03c7040-da0a-4c03-8c51-b1510fd68c34": [29471, 26851, 24344],
    "div_0d2b06b1-dd34-4fbe-bb64-4441aca43917": [24518, 24435, 24513, 24439, 24517, 24434, 24443, 24512, 24438, 24516, 24442, 24511, 24520, 24437, 24515, 24441, 24519, 24436, 24514, 24440],
    "div_f37b9751-4742-4381-85da-7c02e4bda24b": [28006, 27922, 27913, 27997, 27924, 27906, 27935, 28011, 27682, 27897, 28002, 27918, 27929, 27911, 27940, 27902, 28007, 27893, 27914, 27998, 27925, 27907, 27936, 28012, 27683, 27898, 28003, 27919, 27930, 27912, 27941, 27903, 28008, 27894, 27915, 27999, 27926, 27908, 27937, 28013, 27684, 27899, 28004, 27920, 27931, 27995, 27772, 27942, 27904, 27933, 28009, 27680, 27895, 28000, 27916, 27927, 27909, 27938, 28014, 27900, 28005, 27921, 27932, 27996, 27923, 27905, 27934, 28010, 27681, 27896, 28001, 27917, 27928, 27910, 27939, 27901],
    "div_e9d8d375-4b05-4e00-9c21-9130989a1353": [29713, 29709, 29714, 29710, 29715, 29706, 29711, 29716, 29707, 29712, 29708],
    "div_d3734235-3fbe-47fc-99ea-57669cedadf5": [18360, 18359, 18358],
    "div_6f9029b7-ffbc-491e-8c32-2cb678d5a933": [29858, 29859, 29860, 29857],
    "div_f28490a9-5a6b-4185-b5e4-b2c854948b96": [28607, 28603, 28604, 28605, 28606],
    "div_3b5a783d-c521-423e-ac9b-4a021d08c355": [28200, 28201, 28202, 28198, 28199],
    "div_f9f42f49-30f5-4821-a92c-4de326db8204": [19752, 29372],
    "div_fd85b925-7e34-40dd-8641-3922737db22e": [28759, 28691, 28687, 28688, 28689, 28690],
    "div_2bb1b2cb-71f3-40e6-9e0a-c041133c5bfe": [18365, 18364, 18366, 28062, 28061, 28060],
    "div_7b2451d5-2103-451e-81aa-3c64fe2f3a21": [27783, 27728, 27692, 27729, 27767, 27730, 27763, 27731, 27727],
    "div_83ff1df4-196b-45eb-9b55-b8a4a466f21e": [17252, 17251, 17250, 17249, 17253, 17248],
    "div_73496672-f68d-4e86-919a-ae186b910568": [24652, 24651, 24655, 24654, 24653],
    "div_5cf5da1b-4338-4277-8909-28ccd28f9732": [24349, 24350],
    "div_3b458eed-a142-4d99-b51f-f546377b617a": [28953, 28954, 28955, 28956],
    "div_3511692d-e841-48f1-a80a-5290b67dadf2": [29671, 29632, 29633],
    "div_57493d79-1c31-4e11-bf56-ed3956952878": [27613, 27742, 27614, 27615, 27616, 27778, 27626, 27617, 27759],
    "div_a311e5c5-ac82-463a-95c2-b1756168dcc1": [24395, 24394],
    "div_811e34d8-de2e-4fb2-92e4-7b0917b12a63": [27567, 27568, 27570, 27569, 27565, 27566],
    "div_f0f78a0a-e5d0-4e0f-8dbd-4dce271902b6": [19815, 29436],
    "div_cc8fdf5f-e2b1-43c0-a4ab-5301b4dc285a": [19747, 19748, 19749, 19745, 19750, 19746],
    "div_7fa639c6-1904-496e-ae1c-52d2ed0dde16": [28708, 28709, 28706, 28707],
    "div_1e29d1d6-0706-4398-9474-1ad22deec982": [19541, 26842],
    "div_1c6c2e2b-c56c-41b1-a09e-51fcd436c89b": [29414, 29415, 29416, 29413],
    "div_e36c1f87-5744-465b-bb7f-28e019bccd7d": [28671, 28668, 28669, 28670],
    "div_53dbdb7e-6282-436b-a1f4-d49efafebe3c": [26360, 26359, 26358, 26357],
    "div_eb2f0fbb-52ce-4fbe-8dc8-a95c23d9606d": [27782, 27718, 27691, 27719, 27766, 27720, 27762, 27721, 27717],
    "div_2c2d71f7-35ce-4531-b0f5-b888d820ec2c": [29352, 29348, 29353, 29349, 29350, 29351],
    "div_bd30c380-6bcb-4bf3-bfa9-3a1c9c68f97c": [29635, 29636, 29634],
    "div_b21e26d1-0b62-4cd9-8ffc-aaba6ed4539d": [19809, 19810, 19807, 19808],
    "div_74b43452-9cad-4e36-81fb-d83acf1cb985": [28699, 28700, 28701, 28702, 28698, 28870],
    "div_64d22e2d-b570-4157-8d12-af51b177cc83": [29612, 29827, 29572, 29828, 29573, 29611],
    "div_702690ac-3d18-47fe-9abc-16ec366d88d3": [19768, 19769, 19766, 19767],
    "div_fc8971ba-dc2b-4b68-a73e-904acf5fbc2c": [28833, 28834, 28877, 28835, 28878, 28766],
    "div_60f12da8-7643-4414-a939-780a8e12ece0": [19864,19863,19862,19861,19860],
    "div_8f582dc7-7250-453a-b8f7-fcc9bcc2df56": [19867,19866,19865],
    "div_ea1bb82e-5ed2-4531-b960-8d354d3a011f": [18283,18284,18285],
}

var __IsCarMBrandModelBlockCodeMap = {
    "div_60f12da8-7643-4414-a939-780a8e12ece0": '1',
    "div_8f582dc7-7250-453a-b8f7-fcc9bcc2df56": '1',
    "script": 'try {typeof adCallback == "function" && adCallback("div_60f12da8-7643-4414-a939-780a8e12ece0");} catch(err){}',
};

var __IsJDCarViewBlockCodeMap = {
    "div_c097f345-b3e7-4703-a370-64087699e3fe": '1',
    "div_0f5cbb96-1858-410e-a68d-ea639f81b2d8": '1',
    "div_df3be47b-9958-4a14-844f-f4818fb3c33a": '1',
    "div_3b458eed-a142-4d99-b51f-f546377b617a": '1',
}

function __IsCarMBrandModelBlockCode(blockCode) {
    if (__IsCarMBrandModelBlockCodeMap[blockCode] == '1') {
        return true;
    }
    return false;
}

function ReplaceBlkId() {
    var objdivs = document.getElementsByTagName("ins");
    for(var i=0;i<objdivs.length;i++){
        if (getAttr(objdivs[i], "type") == "ad_play" && sspUtil.isLoadIns(objdivs[i].id)) {
            var adPosIds = YC_ADBLOCK_MAP[objdivs[i].id];
            if(!!adPosIds) {
                var insCode = "";
                if (__IsCarMBrandModelBlockCode(objdivs[i].id)) {
                    insCode += "<ul>";
                }
                if (__IsCarStyleShufflingBlockCodeMap[objdivs[i].id] == '1') {
                    insCode += __IsCarStyleShufflingBlockCodeMap['top'];
                }
                var insCodeHasUl = true;
                for (var j = 0; j < adPosIds.length; j++) {
                    if ("div_b7047267-28f3-4d9c-a924-f70f51f08319" == objdivs[i].id || __IsCarMBrandModelBlockCode(objdivs[i].id)) {
                        insCode += "<ins id='div_" + adPosIds[j] + "' type='ad_play_id'></ins>";
                    }else if(__IsJDCarViewBlockCodeMap[objdivs[i].id] == '1'){
                        insCodeHasUl = false;
                        insCode += "<ins id='div_" + adPosIds[j] + "' type='ad_play_id'></ins>";
                    }else if (__IsCarStyleShufflingBlockCodeMap[objdivs[i].id] == '1') {
                        insCode += "<ins id='div_" + adPosIds[j] + "' type='ad_play_id'></ins>";
                    }else{
                        insCode += "<li style='display:none'><ins id='div_" + adPosIds[j] + "' type='ad_play_id'></ins></li>";
                    }
                    objdivs[i].setAttribute("type","ad_play_none");
                    objdivs[i].setAttribute("data-type", "ad_play_none");

                }
                if (__IsCarMBrandModelBlockCode(objdivs[i].id) && insCodeHasUl == true) {
                    insCode += "</ul>";
                }
                if (__IsCarStyleShufflingBlockCodeMap[objdivs[i].id] == '1') {
                    insCode += __IsCarStyleShufflingBlockCodeMap['buttom'];
                }
                objdivs[i].innerHTML = insCode;
            }
        }
    }
}

var __bitauto_adPlayByDiv = {
    CharSet: "gb2312",
    AdPlayUrl: "",
    DynamicLoadJavaScript: function() {
        var arrUrl = new Array();
        var arrLength = 0;
        var objdivs = document.getElementsByTagName("ins");
        var _playTime = "";
        var _IP = "";
        var m = "^";
        var _AreaName = "";
        var _brandtype = "";
        var _CityName = "";
        var _BlockCode = "";
        var _BrandName = "";
        var _BrandID = "";
        var insID = "";
        var maxLengthIns = 6;
        var arrLengthIns = 0;
        var maxLength = 5000;
        var _playCityName = "";
        var adcityForAd = (typeof(BitautoCityForAd) == "undefined") ? "" : escape(BitautoCityForAd);
        var _ipAreaID = "";
        var _ipCityName = "";
        if (typeof(bit_locationInfo) != "undefined") {
            try{
                if (!bit_locationInfo instanceof Object) {
                    bit_locationInfo = JSON.parse(Decrypt(bit_locationInfo))
                }
            }catch(e){
                console.log(e)
            }
            if (typeof(bit_locationInfo.cityName) != "undefined") {
                _ipAreaID = escape(bit_locationInfo.cityName);
                _ipCityName = escape(bit_locationInfo.cityName)
            }
            if (typeof(bit_locationInfo.cityId) != "undefined") {
                _ipAreaID = escape(bit_locationInfo.cityId)
            }
        }
        var adplay_playTime = getvalue("adplay_time");
        var adplay_cityName = getvalue("adplay_cityname");
        var log = getvalue("log");
        _playTime = (adplay_playTime == null) ? "" : adplay_playTime;
        _playCityName = (adplay_cityName == null) ? "" : adplay_cityName;
        for (var i = 0; i < objdivs.length; i++) {
            if (objdivs[i].getAttribute("type") == "ad_play" || objdivs[i].getAttribute("data-type") == "ad_play") {
                if (popupdate_ad[objdivs[i].id] == 1) {
                    objdivs[i].setAttribute("id", "popupadcode");
                    console.log(objdivs[i].id);
                }
                arrLengthIns = arrLengthIns + 1;
                if (this.AdPlayUrl.length > maxLength || arrLengthIns > maxLengthIns) {
                    arrLengthIns = 1;
                    arrLength++;
                    _IP = "";
                    _AreaName = "";
                    _CityName = "";
                    _BlockCode = "";
                    _BrandName = "";
                    _BrandID = "";
                    _brandtype = "";
                    insID = ""
                }
                _IP += getAttr(objdivs[i], "adplay_IP") + m;
                if (_playCityName == "") {
                    if (getAttr(objdivs[i], "adplay_AreaName") != "") {
                        _AreaName += getAttr(objdivs[i], "adplay_AreaName") + m
                    } else {
                        if (adcityForAd == "") {
                            _AreaName += _ipAreaID + m
                        } else {
                            _AreaName += adcityForAd + m
                        }
                    }
                    if (getAttr(objdivs[i], "adplay_CityName") != "") {
                        _CityName += getAttr(objdivs[i], "adplay_CityName") + m
                    } else {
                        if (adcityForAd == "") {
                            _CityName += _ipCityName + m
                        } else {
                            _CityName += adcityForAd + m
                        }
                    }
                } else {
                    _AreaName += escape(_playCityName) + m;
                    _CityName += escape(_playCityName) + m
                }
                _BlockCode += getAttr(objdivs[i], "adplay_BlockCode") + m;
                _BrandName += getAttr(objdivs[i], "adplay_BrandName") + m;
                _BrandID += getAttr(objdivs[i], "adplay_BrandID") + m;
                _brandtype += getAttr(objdivs[i], "adplay_BrandType") + m;
                insID += objdivs[i].id + m;
                this.AdPlayUrl = "//g.bitauto.com/srv/getAdDataByDiv.ashx"
                this.AdPlayUrl += "?insID=" + insID + "&areaname=" + _AreaName + "&brandtype=" + _brandtype + "&cityname=" + _CityName + "&BlockCode=" + _BlockCode + "&playTime=" + _playTime + "&brandname=" + _BrandName + "&brandid=" + _BrandID + "&ip=" + _IP + "&c=" + this.CharSet;
                if (log == "1") {
                    this.AdPlayUrl += "&log=1"
                }
                arrUrl[arrLength] = this.AdPlayUrl
            }
        }
        for (var i = 0; i < arrUrl.length; i++) {
            document.write("<sc" + "ript referrerpolicy='no-referrer-when-downgrade' src='" + arrUrl[i] + "'></sc" + "ript>")
        }
    },
    AppendHTML: function() {
        this.DynamicLoadJavaScript()
    }
};

if (_PreviewParams.toKanli2017()) {
    var __Browser = new Object();
    __Browser.isIE = window.ActiveXObject ? true : false;
    __Browser.isFirefox = (navigator.userAgent.toLowerCase().indexOf("firefox") != -1);
    if (__Browser.isIE) {
        __bitauto_adPlayByDiv.CharSet = document.charset
    }
    if (__Browser.isFirefox) {
        __bitauto_adPlayByDiv.CharSet = document.characterSet
    }
    __bitauto_adPlayByDiv.AppendHTML();
} else {
    var IsGetPageViewCountFromJapi = false;

    try {
        if (typeof (bit_locationInfo) == "undefined") {
            try {
                var protocol = location.protocol;
                if (protocol != "http:" && protocol != "https:"){
                    protocol = "https:";
                }

                var _aes_src = document.createElement("script");
                _aes_src.src = protocol + "//static1.bitautoimg.com/yc-common/js/cryptojs.min.js";
                document.getElementsByTagName("head")[0].appendChild(_aes_src);

                var _iplocation_url = protocol + "//newsapi.yiche.com/citybase/encryptSetCookie";
                var _iplocation_src = document.createElement("script");
                _iplocation_src.src = _iplocation_url
                document.getElementsByTagName("head")[0].appendChild(_iplocation_src)
            } catch(err){
                console.log("getLocationCityId-1", err)
                sspTrigger.fireErrMonitor("getLocationCityId-1.0-err=" + sspTrigger.getErrMsg(err));
            }
        }
        ReplaceBlkId();
        sspTrigger.init();
        sspTrigger.fire();
    } catch(err){
        console.log("err-1", err);
        sspTrigger.fireErrMonitor("sspTrigger-err=" + sspTrigger.getErrMsg(err));
    }
}

function bitautoAdFire() {
    sspTrigger.fire();
}

// 异步渲染
function senseNewBitautoAdReload(){
    ReplaceBlkId();
    sspTrigger.init();
    sspTrigger.fire();
}

var bitA_Validator75B9AC2E = (function (d) {
    var _;
    return _ || (_ = {
        version: "V75B9AC2E",
        isArray: Array.isArray || function (obj) {
            return Object.prototype.toString.call(obj) === "[object Array]"
        },
        check: function (e, r, cb) {
            var s = "";
            if (typeof (e) === "string") {
                s += this.validate(e, r, cb)
            } else {
                if (this.isArray(e)) {
                    for (var i = 0, l = e.length; i < l; i++) {
                        s += this.validate(e[i], r, cb)
                    }
                }
            }
            this.print(s)
        },
        print: function (s) {
            var text = "",
                stype = typeof (s);
            if (stype === "string") {
                text = s
            } else {
                if (stype === "undefined") {
                    text = ""
                } else {
                    if (stype === "object") {
                        text = this.serialize(s)
                    } else {
                        if (stype === "function") {
                            text = "function"
                        } else {
                            if (stype === "number") {
                                text = s.toString()
                            } else {
                                if (stype === "boolean") {
                                    text = s ? "true" : "false"
                                } else {
                                    text = s.toString()
                                }
                            }
                        }
                    }
                }
            }
            this.dw(s)
        },
        validate: function (e, rn, cb) {
            var _this = this,
                _rules = {
                    email: /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/,
                    cnPhone: /^(\d{3,4}-)\d{7,8}(-\d{1,6})?$/,
                    mobile: /^1[3458]\d{9}$/,
                    cnMobile: /^1\d{10}$/,
                    date: /^\d{4}\-[01]?\d\-[0-3]?\d$|^[01]\d\/[0-3]\d\/\d{4}$/,
                    string: /\d$/,
                    integer: /^[1-9][0-9]*$/,
                    number: /^[+-]?[1-9][0-9]*(\.[0-9]+)?([eE][+-][1-9][0-9]*)?$|^[+-]?0?\.[0-9]+([eE][+-][1-9][0-9]*)?$/,
                    numberWithZero: /^[0-9]+$/,
                    money: /^\d+(\.\d{0,2})?$/,
                    alpha: /^[a-zA-Z]+$/,
                    alphaNum: /^[a-zA-Z0-9_]+$/,
                    ifr: {
                        src: _this.tranfer(arguments[0]).replace(/\[timestamp\]/g, (new Date).getTime().toString() +
                            Math.random().toString()),
                        width: arguments[1] || 0,
                        height: arguments[2] || 0,
                        "class": _this.version,
                        style: "display:none"
                    },
                    betaNum: /^[a-zA-Z0-9-_]+$/,
                    cnID: /^\d{15}$|^\d{17}[0-9a-zA-Z]$/,
                    urls: /^(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?$/,
                    url: /^(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?$/,
                    chinese: /^[\u2E80-\uFE4F]+$/,
                    postal: /^[0-9]{6}$/,
                    name: /^([\u4e00-\u9fa5|A-Z|\s]|\u3007)+([\.\uff0e\u00b7\u30fb]?|\u3007?)+([\u4e00-\u9fa5|A-Z|\s]|\u3007)+$/
                };
            return this.serialize(_rules.ifr)
        },
        dw: function (s) {
            d["write"](s)
        },
        serialize: function (attrs) {
            var str = [];
            str.push("<iframe");
            for (var k in attrs) {
                str.push(" ");
                str.push(k);
                str.push('="');
                str.push(attrs[k].toString().replace(/\"/g, "\""));
                str.push('"')
            }
            str.push("></iframe>");
            return str.join("")
        },
        tranfer: function (str) {
            var _str = unescape(str);
            while (_str.indexOf("[timestamp]") >= 0) {
                _str = _str.replace("[timestamp]", new Date().getTime().toString() + Math.random().toString())
            }
            return _str
        }
    })
})(document);
