def test_raises_error_if_register_same_column_multiple_times(self):
        schema = Schema()
        schema.add_producer('my_producer', type='int')
        with self.assertRaises(SchemaError) as ctx:
            schema.add_producer('my_producer', type='int')