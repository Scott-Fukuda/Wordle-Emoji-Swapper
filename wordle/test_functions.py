import introcs
import functions

def test_circumcise():
    print('Testing circumcise')
    input = """Wordle 1,188 5/6 ⬛🟩⬛⬛🟨 ⬛🟩⬛⬛🟨 🟩⬛⬛⬛⬛ ⬛⬛🟨⬛⬛ 🟩🟩🟩🟩🟩"""

    output = """⬛🟩⬛⬛🟨 ⬛🟩⬛⬛🟨 🟩⬛⬛⬛⬛ ⬛⬛🟨⬛⬛ 🟩🟩🟩🟩🟩"""

    introcs.assert_equals(output, functions.circumcise(input))

    input = 'Wordle 1,188 5/6 '
    output = ''
    introcs.assert_equals(output, functions.circumcise(input))

def test_replace():
    print('Testing replace')
    # tests green replacement
    input = """⬛🟩⬛⬛🟨 ⬛🟩⬛⬛🟨 🟩⬛⬛⬛⬛ ⬛⬛🟨⬛⬛ 🟩🟩🟩🟩🟩"""

    output = """⬛😃⬛⬛🟨 ⬛😃⬛⬛🟨 😃⬛⬛⬛⬛ ⬛⬛🟨⬛⬛ 😃😃😃😃😃"""

    introcs.assert_equals(output, functions.replace('🟩', '😃', input))

def test_emoji_swap():
    print('Testing emoji_swap')
    # tests for 5 line replacement
    input = "Wordle 1,188 5/6 ⬛🟩⬛⬛🟨 ⬛🟩⬛⬛🟨 🟩⬛⬛⬛⬛ ⬛⬛🟨⬛⬛ 🟩🟩🟩🟩🟩"
    output = """🥶😃🥶🥶😑 🥶😃🥶🥶😑 😃🥶🥶🥶🥶 🥶🥶😑🥶🥶 😃😃😃😃😃"""
    introcs.assert_equals(output, functions.emoji_swap('😃', '😑', '🥶', input))

test_circumcise()
test_replace()
test_emoji_swap()
print('All tests passed.')
