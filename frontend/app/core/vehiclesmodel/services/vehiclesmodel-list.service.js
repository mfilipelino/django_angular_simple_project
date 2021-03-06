(function(){
	"use strict";

	angular.module('vehiclesmodel').factory('VehiclesModelListService', VehiclesModelListService);


	function VehiclesModelListService(VehiclesModelApi, ManufacturesApi, $q){
		var service = {
			init: init,
			setVehicleModelToEdit: setVehicleModelToEdit,
			deleteVehicleModel: deleteVehicleModel,
			createVehicleModel: createVehicleModel,
			updateVehicleModel: updateVehicleModel,
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
			service.currentVechicleModel = {};

			var defer = $q.defer();
			var promisses = {};
			promisses.manufectures = VehiclesModelApi.getVehiclesModel();
			promisses.vehiclesModel = ManufacturesApi.getManufactures();

			$q.all(promisses).then(function(result){
				service.vehiclesModel = result.manufectures.data.vehicles_models;
				service.manufactures = result.vehiclesModel.data.manufactures;
				defer.resolve(result);
			}, function(erro){
				defer.reject(error);
			});

			return defer.promise;	
		}

		function setVehicleModelToEdit(vehicleModel){			
			var manufacture = GLOBAL.getElementByProperty(service.manufactures, 'id', vehicleModel.manufacturer_id);

			service.currentVechicleModel = {
				id: vehicleModel.id,
				selectedVehicleType: vehicleModel.vehicle_type,
				name: vehicleModel.name,
				selectedMotor: vehicleModel.motor.toString(),
				selectedManufacture: manufacture,

			};
			service.isCreate = false;
		}

		function deleteVehicleModel(vehicleModel){

			var promisse = VehiclesModelApi.deleteVehiclesModelById(vehicleModel.id);

			promisse.then(function(result){
				var indexOfVehicleModel = GLOBAL.indexOfByProperty(service.vehiclesModel, 'id', vehicleModel.id);

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
				promisse = VehiclesModelApi.updateVehicleModel(params);
			}
			else{
				promisse = VehiclesModelApi.saveVehicleModel(params);
			}
			return promisse;
		}

		function createVehicleModel(){

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

		function updateVehicleModel(){

			var promisse = _saveOrCreateVehicleModel(service.currentVechicleModel).then(sucess, error);
			return promisse;

			function sucess(result){
				var data = result.data;
				var vehicleModel = GLOBAL.getElementByProperty(service.vehiclesModel, 'id', data.id);
				Object.assign(vehicleModel, data);
				service.clearEdit();
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