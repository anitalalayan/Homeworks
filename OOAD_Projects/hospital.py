from abc import ABC, abstractmethod

class Patients:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.medical_history = []
        
    def display_med_history(self, medical_operation: 'MedicalOperations'):
        self.medical_history.append(medical_operation)
        
        
class Doctors:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info 
        
    def manage_info(self, patient: 'Patients'):
        pass
    
    
class MedicalStuff:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def manage_hospital_operations(self, operation: 'HospitalOperations'):
        pass
    
class MedicalOperations(ABC):
    @abstractmethod
    def get_operation_details(self):
        pass
    

    
class MedicalProcedures(MedicalOperations):
    def __init__(self, procedure, doctor: 'Doctors'):
        self.procedure = procedure
        self.doctor = doctor 
        
    def get_operation_details(self):
        return f"{self.procedure_type} performed by Dr. {self.doctor.name}"
        

    
class Surgeries(MedicalProcedures):
    def __init__(self, doctor:'Doctors', surgery_type):
        super().__init('Surgery', doctor)                   
        self.surgery = surgery_type
        
    def get_operation_details(self):
        return f"{self.surgery} performed by Dr. {self.doctor.name}"

class Checkups(MedicalProcedures):
    def __init__(self, doctor: 'Doctors'):
        super().__init__('Checkups', doctor)
        
    def get_operation_details(self):
        return f"Checkup performed by Dr. {self.doctor.name}"
