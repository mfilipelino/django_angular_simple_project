(function(){
	'use strict';

	angular.module('manufactures').controller("ManufacturesListController", ManufacturesListController);

	function ManufacturesListController(){
		var $ctrl = this;
		$ctrl.hello = "hello world";
	}

})();