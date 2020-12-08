def test_raises_error_if_specified_producer_is_not_defined(self):
        schema = Schema()
        with self.assertRaises(SchemaError):
            schema.define_column('A', producer='non-existent')