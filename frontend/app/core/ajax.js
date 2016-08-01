"use strict";

angular.module('ajax', []);

angular.module('ajax').config(
    function($httpProvider){
        //Essa configuração pode ser dependente de como seu backend implementa a proteção CSRF
        $httpProvider.defaults.headers.common['X-CSRFToken'] = 'csrftoken'; // alguem precisa ter setado isso aqui!
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    }
);

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
