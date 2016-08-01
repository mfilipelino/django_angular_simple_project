(function(){
	"use-strict";

	angular.module('ajax').config(config);

    function config($httpProvider){
        //Essa configuração pode ser dependente de como seu backend implementa a proteção CSRF
        $httpProvider.defaults.headers.common['X-CSRFToken'] = 'csrftoken'; // alguem precisa ter setado isso aqui!
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    }


})();