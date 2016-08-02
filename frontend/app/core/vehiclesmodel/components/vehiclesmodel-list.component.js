(function(){
	'use strict';

	angular.module('vehiclesmodel').directive('vehiclesmodelList', vehiclesmodelList);  

	function vehiclesmodelList(){

		var component = {
	    	templateUrl: '/static/core/vehiclesmodel/templates/vehiclesmodel-list.template.html',
	    	controller: "VehiclesModelListController",
	    	controllerAs: '$ctrl'
		};

		return component;
	}

})();