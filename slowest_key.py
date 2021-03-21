from typing import List
class SlowestKey:
    def __init__(self, release_time: List[int],key_pressed:str):
        self.release_time = release_time
        self. key_pressed = key_pressed
    
    def run(self):
        times = self.calculate_press_times()
        objects = self.objectify(times)
        objects.sort(key=lambda x: x["time"],reverse=True)
        result = self.check_for_smallest_key_press(objects)
        #print(sorted_objs)
        #print(objects)
        return result["key_pressed"]

    def check_for_smallest_key_press(self,objects):
        current_smallest = objects[0]
        temp = []
        temp.append(current_smallest)
        for i in objects[1:]:
            if(current_smallest["time"]!=i["time"]):
                break
            else:
                temp.append(i)
            temp.sort(key=lambda x: x["key_pressed"],reverse=True)
        return temp[0]

    def objectify(self,times):
        objs = []
        for counter, time in enumerate(times):
            objs.append({
                "time":times[counter],
                "release_time": self.release_time[counter],
                "key_pressed": self.key_pressed[counter]
                })
        return objs
    
    def calculate_press_times(self):
        times = []
        for counter,release in enumerate(self.release_time):
            if(len(self.release_time)) == len(times):
                break
            else:
                if len(times) == 0:
                    times.append(self.release_time[counter])
                times.append(self.release_time[counter+1] - self.release_time[counter])
        return times


""" class KeyObject:
    def __init__(self, release_time, key_pressed, time):
        self.release_time = release_time
        self.key_pressed = key_pressed
        self.time = time

class SlowestKey:
    def __init__(self, release_time: List[int], key_pressed:str):
        self.release_time = release_time
        self.key_pressed = key_pressed
    
    def run(self):
        times = self.find_each_duration()    
        ko = self.classify(times)
        ko.sort(key=lambda x: x.time, reverse=False)
        print(ko)
        
    def classify(self, times):
        keyobjects =  []
        for counter in enumerate(times):
            keyobjects.append(KeyObject(self.release_time[counter],self.key_pressed[counter],time[counter]))            
        return keyobjects

    def find_each_duration(self)->List[int]:
        times = []
        for counter, releases in enumerate(self.release_time):
            if (len(self.release_time)) == len(times):
                break
            else:
                if len(times) == 0:
                    times.append(self.release_time[counter])
                times.append(self.release_time[counter+1] - self.release_time[counter])
        return times
 """