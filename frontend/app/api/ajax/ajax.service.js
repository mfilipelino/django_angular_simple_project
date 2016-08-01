(function(){
	"use strict";

	angular.module('ajax').factory('Ajax', Ajax);


	function Ajax($http){

	    var model = {
	        get: get,
	        post: post
	    };

	    return model;

	    function get(url, params){
	        if(!params){
	            params = {};
	        }
	        return $http({
	            method: 'GET',
	            url: url,
	            params: params //ta vendo, pra GET a gente passa params
	        });
	    }

	    function post(url, params){
	        if(!params){
	            params = {};
	        }
	        return $http({
	            method: 'POST',
	            url: url,
	            data: $.param(params) //e pra post a gente passa data
	        });
	    }
	}

})();