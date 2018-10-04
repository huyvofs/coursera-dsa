# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    size = 10**7
    contacts = [None] * size
    for cur_query in queries:
        index = ((34 * cur_query.number + 2) % 10000019) % size
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if contacts[index] is not None:
                contacts[index].name = cur_query.name
            else:  # otherwise, just add it
                contacts[index] = cur_query
        elif cur_query.type == 'del':
            if contacts[index] is not None:
                contacts[index] = None
            else:
                response = 'not found'
                if contacts[index] is not None:
                    response = contacts[index].name
                    result.append(response)
        return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
