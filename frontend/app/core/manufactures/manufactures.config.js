(function(){
	'use strict';

	angular.module('manufactures').config(config);

	function config($routeProvider) {
      $routeProvider.
        when('/manufactures', {
			template: '<manufectures-list></manufectures-list>',
        });
    }
})();