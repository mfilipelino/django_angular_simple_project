(function(){

	'use strict';

	angular.module('vdfrontend').config(config);

	function config($locationProvider, $routeProvider) {
	  	$locationProvider.html5Mode(true).hashPrefix('!');

  		$routeProvider.otherwise('/manufactures');
	}
	
})();
