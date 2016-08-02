(function(){
	'use strict';

	angular.module('vehicles').controller("VehiclesListController", VehiclesListController);

	function VehiclesListController(VehiclesListService){
		
		var ctrl = this;
		ctrl.service = VehiclesListService;
		ctrl.service.init();

	}

})();


