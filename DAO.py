class DAO():
    @staticmethod
    def getNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """QUERY"""
        cursor.execute(query)

        for row in cursor:
            result.append(Node(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(idNodes):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """QUERY"""
        cursor.execute(query)

        for row in cursor:
            result.append(Edge(idNodes[row['n1']], idNodes[row['n2']], row['weight']))
        cursor.close()
        conn.close()
        return result