import maximum_units_on_a_truck as muoat

def main():
    #temp = muoat.MaximumUnitsOnATruck([[1,3],[2,2],[3,1]],4)
    temp = muoat.MaximumUnitsOnATruck([[5,10],[2,5],[4,7],[3,9]], truckSize = 10)
    print(temp.calculate_units())

if __name__=="__main__":
    main()