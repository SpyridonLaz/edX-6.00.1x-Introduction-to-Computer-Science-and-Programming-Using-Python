import random 
import math
import string
import operator
class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
            self.name = name
            self.species_types = species_types.copy()
            self.location = tuple(float(coords) for coords in location)
    def get_number_of_species(self, animal):
            return self.species_types.get(animal,0)
    def get_location(self):
            return self.location
    def get_species_count(self):
            return self.species_types.copy()
    def get_name(self):
            return self.name
    def adopt_pet(self, species):
            self.species_types[species] -=1
            if self.species_types[species]==0:
                    del self.species_types[species]


list_of_adoption_centers = []
class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
            self.name = name
            self.desired_species = desired_species
    def get_name(self):
            return self.name
    def get_desired_species(self):
            return self.desired_species
    def get_score(self, adoption_center):
            return 1.0*adoption_center.get_number_of_species(self.get_desired_species())

            
class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self,name,desired_species,considered_species):
            self.considered_species = considered_species
            Adopter.__init__(self,name,desired_species)
            
    def get_score(self, adoption_center):
            return Adopter.get_score(self,adoption_center)+0.3*sum ([adoption_center.get_number_of_species(i) for i in self.considered_species])

                


                                                               
class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self,name,desired_species,feared_species):
            
            self.feared_species = feared_species
            Adopter.__init__(self,name,desired_species)

    def get_score(self, adoption_center):
            scores = Adopter.get_score(self,adoption_center)
            total = scores-0.3*adoption_center.get_number_of_species(self.feared_species)
            if total <= 0.0:
                    return 0.0
            return total
            





class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self,name,desired_species,allergic_species):
            self.allergic_species = allergic_species
            Adopter.__init__(self,name,desired_species)

    def get_score(self,adoption_center):
            if len(set(self.allergic_species) &set(adoption_center.get_species_count()  )  )    ==0:
                    return 1.0*adoption_center.get_number_of_species(self.get_desired_species())
            else:
                    return 0.0
                    
            
class MedicatedAllergicAdopter(AllergicAdopter):
    """
    lowest medicine_effectiveness found for these species,
    and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self,name,desired_species,allergic_species,medicine_effectiveness):
            self.medicine_effectiveness = medicine_effectiveness
            AllergicAdopter.__init__(self,name,desired_species,allergic_species)


    def get_score(self,adoption_center):
            tempList = list(set(self.allergic_species) & set( adoption_center.get_species_count()))
            #creates new list type object with all allergic animals that currently exist in Adoption Center
            if tempList ==[]:
                    return 0.0              
            tempDict = {g:self.medicine_effectiveness.get(g,0) for g in tempList}
            # creates dict type object with keys  from tempList and   values from medicine_effectiveness or 0 .
            return Adopter.get_score(self,adoption_center) *tempDict[min(tempDict , key = tempDict.get)]
                            

    





class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def    __init__(self, name, desired_species, location):
            self.desired_species = desired_species
            self.location = location
            Adopter.__init__ (self,name,desired_species)

    def get_linear_distance(self,to_location):
            distance= math.sqrt( (to_location[0]-self.location[0])**2  +  (to_location[1]-self.location[1])**2)
            return distance


                                                                   
    def get_score(self,adoption_center):
            numDesSpecies = adoption_center.get_number_of_species(self.desired_species)
            
            d = self.get_linear_distance(adoption_center.location)
            
            if d <1:
                    return 1.0* numDesSpecies
            elif d<3 and d>=1:
                    return random.uniform(0.7,0.9) *numDesSpecies
            elif d<5 and d>=3:
                    return random.uniform(0.5,0.7) *numDesSpecies
            elif d>=5:
                    return random.uniform(0.1,0.5) *numDesSpecies



    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    abc=[]
    final = []
    for  ac in list_of_adoption_centers:
            tempTuple =  ac , ac.get_name() , adopter.get_score(ac)
            abc.append(tempTuple)

    abc.sort(key=lambda t: (-t[2], t[1]))
    
    for ooo in abc:
            final.append(ooo[0])       
    return final[:]
            


    
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    abc=[]
    final = []
    for  adopter in list_of_adopters:
            tempTuple =  adopter , adopter.get_name() , adopter.get_score(adoption_center)
            abc.append(tempTuple)

    abc.sort(key=lambda t: (-t[2], t[1]))
    abc
    for ooo in abc:
            final.append(ooo[0])       
    return final[:]
            










adopter1 = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 
list_of_adopters=[]
list_of_adoption_centers = []
for i in range(1,7):
        list_of_adopters.append(eval("adopter"+str(i)  ))

del i
ac1 = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))    
for i in range(1,7):
        list_of_adoption_centers.append(eval("ac"+str(i)  ))




##--------------------------

        
q= FlexibleAdopter ("Spyros", "Dog", ["Cat","Bat","Horse","Mouse"] )
w= FearfulAdopter ("Spyros", "Dog", "Cat")
x= SluggishAdopter("spyros","Dog" , (3,4))
b = AllergicAdopter ("Spyros", "Dog", ["Cat","Bat","Horse","Mouse"] )
a = MedicatedAllergicAdopter ("Spyros", "Dog", ["Cat","Bat","Horse","Mouse"] , { "Cat":6.0,"Mouse":6.0,"Bat":6.0, "Horse":2.0})


