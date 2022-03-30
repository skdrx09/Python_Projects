class Time:
    def __init__(self, hours=00, minutes=00, seconds=00):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other_time: object) -> object:
        new_time = Time()

        new_time.seconds = self.seconds + other_time.seconds
        while new_time.seconds >= 60:
            new_time.seconds -= 60
            new_time.minutes += 1
        
        new_time.minutes += self.minutes + other_time.minutes
        while new_time.minutes >= 60:
            new_time.minutes -= 60
            new_time.hours += 1

        new_time.hours += self.hours + other_time.hours
        while new_time.hours >= 24:
            new_time.hours -= 24
        
        return new_time

    def __sub__(self, other_time: object) -> object:
        new_time = Time()
        
        new_time.seconds = self.seconds - other_time.seconds
        while new_time.seconds < 0:
            new_time.seconds += 60
            new_time.minutes -= 1
        
        new_time.minutes += self.minutes - other_time.minutes
        while new_time.minutes < 0:
            new_time.minutes += 60
            new_time.hours -= 1

        new_time.hours += self.hours - other_time.hours
        while new_time.hours < 0:
            new_time.hours += 24
        
        return new_time
    
    def __mul__(self, other_time: object) -> object:
        new_time = Time()

        new_time.seconds = self.seconds * other_time.seconds
        while new_time.seconds >= 60:
            new_time.seconds -= 60
            new_time.minutes += 1
        
        new_time.minutes += self.minutes * other_time.minutes
        while new_time.minutes >= 60:
            new_time.minutes -= 60
            new_time.hours += 1

        new_time.hours += self.hours * other_time.hours
        while new_time.hours >= 24:
            new_time.hours -= 24

        return new_time
    
    def __div__(self, other_time: object) -> object:
        pass

    def __mod__(self, other_time: object) -> object:
        pass

    def __eq__(self, other_time: object) -> bool:
        if self.hours == other_time.hours:
            if self.minutes == other_time.minutes:
                if self.seconds == other_time.seconds:
                    return True
        return False

    def __ne__(self, other_time: object) -> bool:
        if self.hours != other_time.hours:
            if self.minutes != other_time.minutes:
                if self.seconds != other_time.seconds:
                    return True
        return False
    
    def __lt__(self, other_time: object) -> bool:
        if self.hours < other_time.hours:
            if self.minutes < other_time.minutes:
                if self.seconds < other_time.seconds:
                    return True
        return False
    
    def __gt__(self, other_time: object) -> bool:
        if self.hours > other_time.hours:
            if self.minutes > other_time.minutes:
                if self.seconds > other_time.seconds:
                    return True
        return False

    def __le__(self, other_time: object) -> bool:
        if self.hours <= other_time.hours:
            if self.minutes <= other_time.minutes:
                if self.seconds <= other_time.seconds:
                    return True
        return False
    
    def __ge__(self, other_time: object) -> bool:
        if self.hours >= other_time.hours:
            if self.minutes >= other_time.minutes:
                if self.seconds >= other_time.seconds:
                    return True
        return False


def main():
    time1 = Time(1, 20, 30)
    print("Time 1:", time1)
    time2 = Time(22, 41, 31)
    print("Time 2:", time2)
    print("Addition:", time1 + time2)
    print("Subtraction:", time1 - time2)
    print("Multiplication:", time1 * time2)
    

    print(f"Is {time1} equal to {time2}?", time1 == time2)
    print("Are they different times?", time1 != time2)
    print(f"Is {time1} less than {time2}?", time1 < time2)
    print(f"Is {time1} greater than {time2}?", time1 > time2)
    print(f"Is {time1} less or equal than {time2}?", time1 <= time2)
    print(f"Is {time1} greater or equal than {time2}?", time1 >= time2)

if __name__ == "__main__":
    main()

