from curses.ascii import isdigit
import statistics


def process_numbers():
    # Clear the error log
    with open("error_log.txt","w") as file:
        file.write("")
    try:
        with open("numbers.txt", "r") as file:
            sum = 0
            count = 0
            numbers = []
            for line in file:
                line = line.strip()
                count += 1
                if line.isdigit():
                    sum += int(line)
                    numbers.append(int(line))
                else:
                    with open("error_log.txt","a") as file:
                        file.write(f"Warrning: line {count} of numbers.txt - {line} is not a number\n")   
                    continue
            average_num = statistics.mean(numbers)
            max_num = max(numbers)
            min_num = min(numbers)
            print(average_num,max_num,min_num)
        with open("report.txt", "w") as file:
            file.write(f"Report:\n")
            file.write("-------\n")
            file.write(f"Count: {count}\n")
            file.write(f"Sum: {sum}\n")
            file.write(f"Average: {average_num}\n")
            file.write(f"Minimum: {min_num}\n")
            file.write(f"Maximum: {max_num}\n")
        with open("sum.txt", "w") as file:
            file.write(str(sum))
            print("The sum of the numbers in the file is:",sum," And the sum has been written to sum.txt")
    except FileNotFoundError as e:
        print("File not found. Please check the file name and try again.",e)
        with open("error_log.txt","a") as file:
            file.write()
    finally:
        print("File Processing Complete.")

if __name__ == "__main__":
    process_numbers()