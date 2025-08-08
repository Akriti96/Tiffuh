'''
Scenario:
A smart thermostat system reads temperature and adjusts air conditioning accordingly. Temperature values should not be directly set from outside the system (e.g., by hackers or bugs).

Task:
Create a SmartThermostat class where temperature is private. Only trusted internal methods should change it.
'''


'''
Scenario:
In an online learning platform, student grades should not be changed or viewed by unauthorized users.

Task:
Create a Student class that encapsulates grades, allowing only teachers to view or modify them.
'''


'''
Scenario:
In an e-commerce platform, stock quantity should not be accessed directly. Only the system should be able to update it on order or return.

Task:
Create a Product class to encapsulate stock quantity with limited access.
'''


'''
Scenario:
You are building a hospital management system. Patient medical records (diagnosis, treatment history) must remain confidential and not exposed directly. 
Only internal processes like treatment updates or internal audits should have access.
You must avoid traditional getter/setter methods and still maintain strict encapsulation.

Task:
Design a class PatientRecord where:
Records are stored privately.
Only authenticated internal methods (like add_treatment() and audit()) can access/update them.
Direct access from outside the class is completely blocked.
'''

'''
Scenario:
You’re developing a FinTech risk analysis engine. The credit score of a client must not be read or modified directly. 
The score is updated based on internal logic (like timely payment or default). There should be no external access, 
and the logic should autonomously manage the score.

Task:
Create a CreditProfile class that:
Stores __credit_score privately
Allows score updates via internal logic only
Prevents outside interference or reading of the score
'''