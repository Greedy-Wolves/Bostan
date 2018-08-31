import bs4


class DecodedCourse(object):
    """
    Data type for Storing parsed and decoded Course

    Attributes
    ----------
    code : str
        course code in xxyyyyy-zz format. xx for department id and zz for group id
    name : str
        the name of the course
    unit_count : int
        total number of unit for this course
    gender: bool
        course gender spec.
        True for men only, False for women only and None for mixed courses
    instructor : str
        name of course instructors. split by `,` character
    days_times : list
        list of day_time that course will be hold.
        every day_time is a tuple with this format, (day_number, start_time, end_time)
    """
    def __init__(self, code, name, unit_count, gender, professor, days_times):
        self.code = code
        self.name = name
        self.unit_count = DecodedCourse.__stardandize_course_units__(unit_count)
        self.gender = DecodedCourse.__stardandize_gender__(gender)
        self.instructor = professor
        self.days_times = DecodedCourse.__stardandize_days_times__(days_times)

    @staticmethod
    def __stardandize_course_units__(course_unit_string):
        if course_unit_string == '۰/۵':
            course_unit_string = '۱'

        return int(course_unit_string)

    @staticmethod
    def __stardandize_gender__(gender_string):
        if gender_string == 'مختلط':
            return None
        if gender_string == 'زن':
            return False
        if gender_string == 'مرد':
            return True

    @staticmethod
    def __stardandize_days_times__(days_times_string):
        days_times = []

        lines = days_times_string.split('\n')
        for line in lines:
            if line.strip().startswith('درس'):
                line = line.split(":", 1)[1]
                day, time = line.split("شنبه", 1)
                day = day.strip()
                std_day = DecodedCourse.__standardize_weekday__(day)
                time = time.strip()[:11]

                time1, time2 = time.split('-', 1)
                std_time1 = DecodedCourse.__standardize_time__(time1)
                std_time2 = DecodedCourse.__standardize_time__(time2)
                days_time = (std_day, std_time1, std_time2)
                days_times.append(days_time)

        return days_times

    @staticmethod
    def __standardize_weekday__(weekday_string):
        if weekday_string == '':
            return 0
        if weekday_string == 'يك':
            return 1
        if weekday_string == 'دو':
            return 2
        if weekday_string == 'سه':
            return 3
        if weekday_string == 'چهار':
            return 4
        if weekday_string == 'پنج':
            return 5

    @staticmethod
    def __standardize_time__(time_string):
        hour, minute = time_string.split(":")
        return "{:02d}:{:02d}".format(int(hour), int(minute))


def parse_page(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    for table in soup.find_all('table', id='Table3'):
        for row in parse_table(table):
            yield decode_row(row)


def parse_table(table):
    return table.find_all('tr', style="")


def parse_row(row):
    items = []
    for item in row.find_all('td'):
        items.append(item)
    extracted_items = [
        items[0].find('div', dir="ltr").get_text(),  # code
        items[1].get_text(),  # name
        items[2].find('nobr', dir="ltr").get_text(),  # all_units
        items[3].find('nobr', dir="ltr").get_text(),  # work_units
        items[4].get_text(),  # zarfiat
        items[5].get_text(),  # por shode
        items[6].get_text(),  # entezar
        items[7].get_text(),  # gender
        items[8].get_text(','),  # professor
        items[9].get_text('\n'),  # time and location
        items[14].get_text()  # hazf pazir
    ]
    return extracted_items


def decode_row(row):
    parsed_row = parse_row(row)
    decoded_course = DecodedCourse(
        code=parsed_row[0],
        name=parsed_row[1],
        unit_count=parsed_row[2],
        gender=parsed_row[7],
        professor=parsed_row[8],
        days_times=parsed_row[9]
    )
    return decoded_course


def main():
    decoded_courses = []
    with open('samples/Courses_962.html', 'r') as file:
        soup = bs4.BeautifulSoup(file.read(), 'html.parser')
        table = soup.find_all('table', id='Table3')[0]
        for row in parse_row(table):
            decoded_courses.append(decode_row(row))
    print(decoded_courses)


if __name__ == '__main__':
    main()
