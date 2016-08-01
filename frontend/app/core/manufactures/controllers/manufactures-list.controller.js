(function(){
	'use strict';

	angular.module('manufactures').controller("ManufacturesListController", ManufacturesListController);

	function ManufacturesListController(ManufacturesListService){
		var ctrl = this;
		ctrl.service = ManufacturesListService;
		ctrl.service.init();
	}

})();