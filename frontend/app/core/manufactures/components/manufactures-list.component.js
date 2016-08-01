(function(){
	'use strict';

	angular.module('manufactures').directive('manufecturesList', manufecturesList);  

	function manufecturesList(){

		var component = {
	    	templateUrl: '/static/core/manufactures/templates/manufactures-list.template.html',
	    	controller: "ManufacturesListController",
	    	controllerAs: '$ctrl'
		};

		return component;
	}

})();