(function(){
	'use strict';

	angular.module('vehicles').directive('vehiclesList', vehiclesList);  

	function vehiclesList(){

		var component = {
	    	templateUrl: '/static/core/vehicles/templates/vehicles-list.template.html',
	    	controller: "VehiclesListController",
	    	controllerAs: '$ctrl'
		};

		return component;
	}

})();