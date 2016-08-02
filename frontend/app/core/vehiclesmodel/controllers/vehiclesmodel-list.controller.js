(function(){
	'use strict';

	angular.module('vehiclesmodel').controller("VehiclesModelListController", VehiclesModelListController);

	function VehiclesModelListController(VehiclesModelListService){
		
		var ctrl = this;
		ctrl.service = VehiclesModelListService;
		ctrl.service.init();

	}

})();


