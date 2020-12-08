 def test_can_obtain_a_column_type(self):
        schema = Schema()
        schema.define_column('A', type='int')
        self.assertEqual(('A',), schema.columns)
        self.assertEqual('A', schema.producers[0].name)
        self.assertEqual('int', schema.producers[0].type)
        self.assertEqual({}, schema.producers[0].config)