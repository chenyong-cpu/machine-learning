/*!
 * jQuery-ajaxTransport-XDomainRequest - v1.0.4 - 2015-03-05
 * https://github.com/MoonScript/jQuery-ajaxTransport-XDomainRequest
 * Copyright (c) 2015 Jason Moon (@JSONMOON)
 * Licensed MIT (/blob/master/LICENSE.txt)
 */
function IEAjaxInit(){
	(function(a){if(typeof define==='function'&&define.amd){define(['jquery'],a)}else if(typeof exports==='object'){module.exports=a(require('jquery'))}else{a(jQuery)}}(function($){if($.support.cors||!$.ajaxTransport||!window.XDomainRequest){return $}var n=/^(https?:)?\/\//i;var o=/^get|post$/i;var p=new RegExp('^(\/\/|'+location.protocol+')','i');$.ajaxTransport('* text html xml json',function(j,k,l){if(!j.crossDomain||!j.async||!o.test(j.type)||!n.test(j.url)||!p.test(j.url)){return}var m=null;return{send:function(f,g){var h='';var i=(k.dataType||'').toLowerCase();m=new XDomainRequest();if(/^\d+$/.test(k.timeout)){m.timeout=k.timeout}m.ontimeout=function(){g(500,'timeout')};m.onload=function(){var a='Content-Length: '+m.responseText.length+'\r\nContent-Type: '+m.contentType;var b={code:200,message:'success'};var c={text:m.responseText};try{if(i==='html'||/text\/html/i.test(m.contentType)){c.html=m.responseText}else if(i==='json'||(i!=='text'&&/\/json/i.test(m.contentType))){try{c.json=$.parseJSON(m.responseText)}catch(e){b.code=500;b.message='parseerror'}}else if(i==='xml'||(i!=='text'&&/\/xml/i.test(m.contentType))){var d=new ActiveXObject('Microsoft.XMLDOM');d.async=false;try{d.loadXML(m.responseText)}catch(e){d=undefined}if(!d||!d.documentElement||d.getElementsByTagName('parsererror').length){b.code=500;b.message='parseerror';throw'Invalid XML: '+m.responseText;}c.xml=d}}catch(parseMessage){throw parseMessage;}finally{g(b.code,b.message,c,a)}};m.onprogress=function(){};m.onerror=function(){g(500,'error',{text:m.responseText})};if(k.data){h=($.type(k.data)==='string')?k.data:$.param(k.data)}m.open(j.type,j.url);m.send(h)},abort:function(){if(m){m.abort()}}}});return $}));
}
IEAjaxInit()

var DASCoinAdvert = {
	prefix: 'ecoin',
	cdnUrl: '//img.easypass.cn/das/cheyingtong/adsense/prod/',
	statisticsUrl: '//jwechatapi.yichehuoban.cn/statistics/yiche/adEffect',
	pageIds: {
        '0e1e2663-364f-45bb-b53f-cdf3de666c32' : {
			url: "yiche_pc_home.js",
			serverId: 3
		},
        'b73f9e35-64fb-4cab-ab73-d8b7d683802a' : {
			url: "yiche_m_news.js",
			serverId: 4
		},
		'20fd8a8b-b46f-431b-9e9a-79def221bca7': {
			url: "yiche_pc_news.js",
			serverId: 5
		},
		'81a2f8d7-5171-408f-9b49-8c582f28505e' : {
			url: 'yiche_m_choosecar.js',
			serverId: 6
		},
		'a1c224ab-6f38-4108-917a-8249daaf73b2' : {
			url: 'yiche_pc_city.js',
			serverId: 7
		},
		'f7dc5af9-f880-4ff8-bd34-733b4c46f4cd' : {
			url: 'yiche_pc_search.js',
			serverId: 8
		},
		'e4416b60-b1a7-4b00-934e-ef6c038ca118' : {
			url: 'yiche_m_common.js',
			serverId: 9
		},
		'3d4960bf-d0bc-4b90-a554-47bc351fa864' : {
			url: 'yiche_pc_common.js',
			serverId: 10
		},
		'ac23c817-c2f5-4c57-bbb0-05a81e2c41f1' : {
			url: 'baojia_app.js',
			serverId: 11
		},
		'29e209e0-1421-746f-a87c-e2ff144ccf58' : {
			url: 'yiche_m_kj_choosecar.js',
			serverId: 12
		}
	},
	baseUrl: '//cytcache.easypass.cn/open/front/get',
	posLogMap:{},
	init: function () {
		var $this = this;
		var pageId = "";

		$("ins[id^="+$this.prefix+"]").each(function() {
			var ins = $(this);
			pageId = ins.attr("pageid");
			pageUrl = $this.cdnUrl + $this.pageIds[pageId].url + '?v=' +(new Date()).getTime();

			$.getScript(pageUrl, function () {
				if (typeof DASCoinAdvertPage == 'object') {
					$this.ecoin_controller.register(DASCoinAdvertPage);
				}

				$this.render(ins.attr("id"),  ins.attr("pageid"),ins.attr("cityid"),
					ins.attr("positionid"), ins.attr("csid"));
			})
		})

		$this.statisticsClick();
	},
	/**
     * jsonp GET 请求
     * @param {string} strUrl 接口地址
     * @param {object} objParam 请求参数
     * @param {string} fname 回调函数名
     * @param {function} callback 回调函数
     */
    JsonpGet: function(strUrl, objParam, fname, callback, retryCount) {
        var destUrl = strUrl;
        this[fname] = callback;
		var $this = this;
		$.ajax({
			url: destUrl,
			type: "Get",
			cache: false,
			dataType: "json",
			success: function (data) {
				DASCoinAdvert[fname](data);
			},
			error: function (e) {
				retryCount = retryCount || 0;
				if(retryCount < 10) {
					IEAjaxInit();
					setTimeout(function(){
						$this.JsonpGet(strUrl, objParam, fname, callback, retryCount + 1);
					}, 500);
				}
				else {
					DASCoinAdvert[fname](null);
				}
			}
		});
    },
	render: function (insId, pageId, cityId, positionId, csId) {
		var $this = this;
		//由于和以前的默认广告的positionId冲突，把2005改成2006了
		if(positionId=="2005"){
			positionId="2006";
		}
		var destUrl = $this.baseUrl + '/'+cityId+'/'+positionId;
		destUrl += csId ? '/'+csId : '';
		//destUrl += "?t="+ $this.format(new Date(), "yyyyMMdd");

		//csid=0表示有空车型占位，直接展示默认结构
		if(csId == "0") {
			$this.buildHtml({}, positionId, insId);
			return;
		}

		var req_data = null;

		var callbackName = "_" + cityId + "_" + positionId;

		$this.JsonpGet(destUrl, req_data, callbackName, function(result) {
			var isSuccess = $this.buildHtml(result, positionId, insId);
			if(isSuccess) {
				var log = {
					PageId: $this.pageIds[pageId].serverId,
					Position: positionId,
					DealerID: result.data[0].dealerId,
					NewsID: result.data[0].advertId,
					CityID: cityId
				}

				if(log.DealerID && log.DealerID != 'null' && log.NewsID && log.NewsID != 'null' && !result.data[0].isDefault) {
					$this.statisticsLoad(log);
					$this.posLogMap[positionId] = log;
				}
			}
		})
	},
	/**
	 * 生成html广告
	 * @param {object} result 
	 * @param {int} positionId 位置Id
	 * @param {string} insId 容器Id
	 */
	buildHtml:function(result, positionId, insId) {
	    if (typeof DASCoinAdvertPage == 'object') {

			var data = result ? result.data : null;

			if (!result || result.status != 1 || !result.data || result.data == 'null') {
				data = null;
			}

			var advertdata = this.ecoin_controller.renderHtml(positionId, data);
			if (advertdata && advertdata.html) {
				$("#" + insId).html(advertdata.html);
				return advertdata.hasAdvert;
			}
		}

		return false;
	},
	/**
	 * 统计曝光量
	 * @param {object} log 
	 */
	statisticsLoad: function (log) {
		log.ProjectId = 101;
		this.statisticsCore(log);
	},
	/**
	 * 统计点击量
	 */
	statisticsClick: function () {
		var $this = this;
		$(document).off("click", "[data-eadvposid]").on("click", "[data-eadvposid]", function(e) {
			
			var posid = $(this).attr("data-eadvposid");
			var log = $this.posLogMap[posid];
			if(log) {
				log.ProjectId = 102;
				$this.statisticsCore(log);
			}
		});
	},
	/**
	 * 调用统计接口
	 * @param {object} log 
	 */
	statisticsCore: function(log) {
		log.URL = document.URL;
		log.Reffer = document.referrer;
		log.Cookie = ((typeof XCWEBLOG_ID == "undefined") || !XCWEBLOG_ID) ? '' : XCWEBLOG_ID;
		log.CreateTime = this.format(new Date(), "yyyy-MM-dd hh:mm:ss")

		//$.ajax({
		//	url: this.statisticsUrl,
		//	type: "POST",
		//	data: JSON.stringify(log),
		//	contentType: "application/json",
		//	dataType: "json",
		//	cache:false,
		//	timeout: 30000,
		//	success: function (response) {
		//	},
		//	error: function () {
	
		//	}
		//});

		
	},
	 format : function(date, format) {
		var year = date.getFullYear();
		var month = date.getMonth() + 1;
		var day = date.getDate();
		var hour = date.getHours();
		var minute = date.getMinutes();
		var seconds = date.getSeconds();
		var oriformat = format;
	
		oriformat = oriformat.replace(/yyyy/g, year);
		oriformat = oriformat.replace(/MM/g, (month > 9 ? month : "0" + month));
		oriformat = oriformat.replace(/dd/g, (day > 9 ? day : "0" + day));
		oriformat = oriformat.replace(/hh/g, (hour > 9 ? hour : "0" + hour));
		oriformat = oriformat.replace(/mm/g, (minute > 9 ? minute : "0" + minute));
		oriformat = oriformat.replace(/ss/g, (seconds > 9 ? seconds : "0" + seconds));
	
		oriformat = oriformat.replace(/M/g, month);
		oriformat = oriformat.replace(/d/g, day);
		oriformat = oriformat.replace(/h/g, hour);
		oriformat = oriformat.replace(/m/g, minute);
		oriformat = oriformat.replace(/s/g, seconds);
	
		return oriformat;
	},
	ecoin_controller : {
		pages:[],
		register: function(page) {
			for(var i in this.pages) {
				if(this.pages[i] == page) {
					return false;
				}
			}
	
			this.pages.push(page);
			return true;
		},
		renderHtml: function(positionId, data) {
			for(var i in this.pages) {
				if(this.pages[i].renderHtml) {
					var html = this.pages[i].renderHtml(positionId, data);
					if(html) {
						return html;
					}
				}
			}
			return undefined;
		}
	}
}

DASCoinAdvert.init();