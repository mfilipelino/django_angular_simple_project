(function(){
	"use strict";

	angular.module('vehicles').factory('VehiclesListService', VehiclesListService);


	function VehiclesListService(VehiclesApi, VehiclesModelApi, $q){

		var service = {
			init: init,
			setVehicleToEdit: setVehicleToEdit,
			deleteVehicle: deleteVehicle,
			createVehicle: createVehicle,
			updateVehicle: updateVehicle,
			clearEdit: clearEdit,
			clearSearch: clearSearch,
			changeVehicleModelFilter: changeVehicleModelFilter
		};

		return service;

		function init(){
			service.vehiclesModel = [];
			service.isCreate = true;
			service.selectManufacture = {};
			service.colorChoice = ['blue', 'black', 'red'];
			service.vehicleYearChoice = GLOBAL.getYearArrayRange(2000, 2016);
			service.search = {};
			service.currentVechicle = {};

			var defer = $q.defer();
			var promisses = {};
			promisses.vehicles = VehiclesApi.getVehicles();
			promisses.vehiclesModel = VehiclesModelApi.getVehiclesModel();

			$q.all(promisses).then(function(result){
				service.vehicles = result.vehicles.data.vehicles;
				service.vehiclesModel = result.vehiclesModel.data.vehicles_models;
				defer.resolve(result);
			}, function(error){
				defer.reject(error);
			});

			return defer.promise;	
		}

		function setVehicleToEdit(vehicle){			
			var model = GLOBAL.getElementByProperty(service.vehiclesModel, 'id', vehicle.vehicle_model_id);

			service.currentVehicle = {
				id: vehicle.id,
				selectedColor: vehicle.color,
				selectedYear: vehicle.year,
				selectedVehicleModel: model,
				selectedMileage: vehicle.mileage,

			};
			service.isCreate = false;
		}

		function deleteVehicle(vehicle){

			var promisse = VehiclesApi.deleteVehiclesById(vehicle.id);

			promisse.then(function(result){
				var indexOfVehicleModel = GLOBAL.indexOfByProperty(service.vehicles, 'id', vehicle.id);

				var deletedVehicleVector = service.vehicles.splice(indexOfVehicleModel, 1);
				var deletedVehicle = deletedVehicleVector[0];

				if(service.currentVechicle.id === deletedVehicle.id){
					service.clearEdit();
				}
			});
			return promisse;
		}

		function _saveOrCreateVehicleModel(vehicle){

			var vehicle_params = {
				id: vehicle.id,
				color: vehicle.selectedColor,
				year: vehicle.selectedYear,
				mileage: vehicle.selectedMileage, 
				vehicle_model_id: vehicle.selectedVehicleModel.id,
			};

			var params = {
				vehicle_dict: vehicle_params,
			};

			var promisse;

			if(vehicle_params.id){
				promisse = VehiclesApi.updateVehicle(params);
			}
			else{
				promisse = VehiclesApi.saveVehicle(params);
			}
			return promisse;
		}

		function createVehicle(){

			var promisse = _saveOrCreateVehicleModel(service.currentVehicle).then(sucess, error);
			return promisse;

			function sucess(result){
				service.vehicles.push(result.data);
				service.clearEdit();
			}

			function error(result){
				alert(result.data);
			}
		}

		function updateVehicle(){

			var promisse = _saveOrCreateVehicleModel(service.currentVehicle).then(sucess, error);
			return promisse;

			function sucess(result){
				var data = result.data;
				var vehicle = GLOBAL.getElementByProperty(service.vehicles, 'id', data.id);
				Object.assign(vehicle, data);
				service.clearEdit();
			}

			function error(result){
				alert(result.data);
			}

		}

		function clearEdit(){
			service.currentVehicle = {};
			service.isCreate = true;
		}

		function clearSearch(){
			service.search = {};
			service.manufacturerFilter = null;
		}

		function changeVehicleModelFilter(){
			service.search.vehicle_model_id = service.vehicleModelFilter.id;
		}
	}

})();