def person_info(country, city, mail, phone, surname, name, birthday):
    return f'Country - {country}; City - {city}; mail - {mail}; phone - {phone}, ' \
           f'Surname - {surname}, Name - {name}, birthday - {birthday}'


print(person_info(surname='Иванов', name='Иван', birthday='01.01.1901 г.р.',
                  country='Россия', city='Улушта', mail='ivanov@ivan.ru', phone='123456789'))
