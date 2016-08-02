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
			changeManufacturerFilter: changeManufacturerFilter
		};

		return service;

		function init(){
			service.vehiclesModel = [];
			service.isCreate = true;
			service.selectManufacture = {};
			service.vehicleTypeChoice = ['car', 'bike'];
			service.motorChoice =  ["125", "250", "500", "1000", "1200", "1400", "1600", "1800", "2000"];
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

			service.currentVechicle = {
				id: vehicle.id,
				selectedColor: vehicle.color,
				selectedYear: vehicle.year,
				selectedVehicleModel: model.name,
				selectedMileage: vehicle.mileage,

			};
			service.isCreate = false;
		}

		function deleteVehicle(vehicleModel){

			var promisse = VehiclesModelApi.deleteVehiclesModelById(vehicleModel.id);

			promisse.then(function(result){
				var indexOfVehicleModel = GLOBAL.indexOfByProperty(service.vehicles, 'id', vehicleModel.id);

				var deletedVehicleModelVector = service.vehiclesModel.splice(indexOfVehicleModel, 1);
				var deletedVehicleModel = deletedVehicleModelVector[0];

				if(service.currentVechicleModel.id === deletedVehicleModel.id){
					service.clearEdit();
				}
			});
			return promisse;
		}

		function _saveOrCreateVehicleModel(vehicleModel){

			var vehiclemodel_params = {
				id: vehicleModel.id,
				name: vehicleModel.name,
				manufacturer_id: vehicleModel.selectedManufacture.id,
				motor: vehicleModel.selectedMotor,
				vehicle_type: vehicleModel.selectedVehicleType, 
			};

			var params = {
				vehiclemodel_dict: vehiclemodel_params,
			};

			var promisse;

			if(vehiclemodel_params.id){
				promisse = VehiclesModelApi.updateVehicle(params);
			}
			else{
				promisse = VehiclesModelApi.saveVehicleModel(params);
			}
			return promisse;
		}

		function createVehicle(){

			var promisse = _saveOrCreateVehicleModel(service.currentVechicleModel).then(sucess, error);
			return promisse;

			function sucess(result){
				service.vehiclesModel.push(result.data);
				service.clearEdit();
			}

			function error(result){
				alert(result.data);
			}
		}

		function updateVehicle(){

			var promisse = _saveOrCreateVehicleModel(service.currentVechicleModel).then(sucess, error);
			service.clearEdit();
			return promisse;

			function sucess(result){
				var data = result.data;
				var vehicleModel = GLOBAL.getElementByProperty(service.vehiclesModel, 'id', data.id);
				Object.assign(vehicleModel, data);
			}

			function error(result){
				alert(result.data);
			}

		}

		function clearEdit(){
			service.currentVechicleModel = {};
			service.isCreate = true;
		}

		function clearSearch(){
			service.search = {};
			service.manufacturerFilter = null;
		}

		function changeManufacturerFilter(){
			service.search.manufacturer_id = service.manufacturerFilter.id;
		}
	}

})();