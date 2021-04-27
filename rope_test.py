from rope import delete_range, insert, create_rope_from_map, rebalance
import unittest


def create_leaf(text):
    return create_rope_from_map({"text": text})


# These tests are here as a starting point, they are not comprehensive
class Testing(unittest.TestCase):
    def test_rope_basics(self):
        self.assertEqual(create_leaf("test").to_string(), "test")
        self.assertEqual(create_leaf("test").size(), 4)
        branch = create_rope_from_map(
            {
                "left": {
                    "left": {"text": "t"},
                    "right": {"text": "e"},
                },
                "right": {"right": {"text": "st"}},
            }
        )
        self.assertEqual(branch.to_string(), "test")
        self.assertEqual(branch.size(), 4)

    def test_deletion(self):
        self.assertEqual(delete_range(create_leaf("test"), 1, 3).to_string(), "tt")
        self.assertEqual(delete_range(create_leaf("test"), 2, 4).to_string(), "te")
        self.assertEqual(delete_range(create_leaf("test"), 0, 2).to_string(), "st")

    def test_insertion(self):
        self.assertEqual(insert(create_leaf("test"), "123", 2).to_string(), "te123st")
        self.assertEqual(insert(create_leaf("test"), "123", 4).to_string(), "test123")
        self.assertEqual(insert(create_leaf("test"), "123", 0).to_string(), "123test")

    def test_extra_credit_rebalancing(self):
        self.assertEqual(
            rebalance(
                create_rope_from_map(
                    {
                        "left": {"text": "a"},
                        "right": {
                            "left": {"text": "b"},
                            "right": {"left": {"text": "c"}, "right": {"text": "d"}},
                        },
                    }
                )
            ).to_dictionary(),
            {
                "left": {"left": {"text": "a"}, "right": {"text": "b"}},
                "right": {"left": {"text": "c"}, "right": {"text": "d"}},
            },
        )


if __name__ == "__main__":
    unittest.main()
