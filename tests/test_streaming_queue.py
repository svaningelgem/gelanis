import tornado.testing

import gelanis


class TestCount(tornado.testing.AsyncTestCase):

    def test_count(self):
        sc = gelanis.Context()
        ssc = gelanis.streaming.StreamingContext(sc, 0.1)

        result = []
        (
            ssc.queueStream([range(20), ['a', 'b'], ['c']])
            .count()
            .foreachRDD(lambda rdd: result.append(rdd.collect()[0]))
        )

        ssc.start()
        ssc.awaitTermination(timeout=0.35)
        self.assertEqual(sum(result), 23)

    def test_groupByKey(self):
        sc = gelanis.Context()
        ssc = gelanis.streaming.StreamingContext(sc, 0.1)

        result = []
        (
            ssc.queueStream([[('a', 5), ('b', 8), ('a', 2)],
                             [('a', 2), ('b', 3)]])
            .groupByKey().mapPartitions(sorted).mapValues(sorted)
            .foreachRDD(lambda rdd: result.append(rdd.collect()))
        )

        ssc.start()
        ssc.awaitTermination(timeout=0.25)
        self.assertEqual(
            result, [[('a', [2, 5]), ('b', [8])], [('a', [2]), ('b', [3])]])

    def test_mapValues(self):
        sc = gelanis.Context()
        ssc = gelanis.streaming.StreamingContext(sc, 0.1)

        result = []
        (
            ssc.queueStream([[('a', [5, 8, 2]), ('b', [6, 3, 8])]])
            .mapValues(sorted)
            .foreachRDD(lambda rdd: result.append(rdd.collect()))
        )

        ssc.start()
        ssc.awaitTermination(timeout=0.15)
        self.assertEqual(result, [[('a', [2, 5, 8]), ('b', [3, 6, 8])]])
