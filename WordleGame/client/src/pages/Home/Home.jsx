import React from "react"
import "./Home.css"
const Home = () => {
    const inputRefs = useRef([])
    const targetWord = "fuffy"
    const targetWordArr = targetWord.split("")

    const [numberOfLetters, setNumberOfLetters] = useState(5)
    const wordSet = {
        5: "board",
        6: "kousik",
        7: "nehanth",
        8: "krishnan",
    }
    const selectedWord = wordSet[numberOfLetters] // Target Word get selected randomly
    const selectedWordArr = selectedWord.split("")

    const handleInput = () => {
        console.log(inputRefs.current)
        const value = e.target.value
        const updatedInput = [...userInput]
        updatedInput[columnIndex] = value
        setuserInput(updatedInput)
        if (value && columnIndex < selectedWordArr.length - 1) {
            console.log("ccccccc" + columnIndex + 1)
            inputRefs.current[rowIndex][columnIndex + 1].disabled = false
            inputRefs.current[rowIndex][columnIndex + 1].focus()
        }
    }

    // Creating input cells
    const rows = []
    for (let i = 0; i < selectedWordArr.Length + 1; i++) {
        // Rows
        rows.push(
            <div className="input-field" key={i}>
                {/* Columns */}
                {selectedWordArr.map((letter, columnIndex) => (
                    <input
                        type="text"
                        key={columnIndex}
                        id={`${i}-${columnIndex}`}
                        t
                        onChange={(e) => handleInput(e, columnIndex, i)}
                        maxLength={1}
                        disabled={!(i === 0 && columnIndex === 0)}
                        // ref={(el) => (inputRefs.current[columnIndex] = el)}
                        ref={(el) => {
                            inputRefs.current[i] = inputRefs.current[i] || []
                            inputRefs.current[i][columnIndex] = el
                        }}
                    />
                ))}
            </div>
        )
    }

    const handleSubmit = () => {
        e.preventDefault()

        const inlcudedLetters = []
        const correctLetters = []

        userInput.map((userLetter, index) => {
            if (targetWordArr.includes(userLetter)) {
                inlcudedLetters.push(userLetter)
                inputRefs.current[rowUnlocked - 1][index].className = "included-letters"
            } else {
                inputRefs.current[rowUnlocked - 1][index].className = "missing-letters"
            }
        })

        for (let index = 0; index < targetWordArr.length; index++) {
            if (userInput[index] == targetWordArr[index]) {
                correctLetters.push(userInput[index])
                inputRefs.current[rowUnlocked - 1][index].className = "correct-letters"
            }
        }

        // Unlocking next row and disabling previous row
        for (let index = 0; index < targetWordArr.length; index++) {
            inputRefs.current[rowUnlocked - 1][index].disabled = true
        }
        if (rowUnlocked < targetWordArr.length + 1) {
            inputRefs.current[rowUnlocked][0].disabled = false
            inputRefs.current[rowUnlocked][0].focus()
            setrowUnlocked((prev) => prev + 1)
        }

        setTimeout(() => {
            if (JSON.stringify(userInput) == JSON.stringify(targetWordArr)) {
                alert("Success. You found the word")
            }
        }, 500)
    }
    return (
        <div className="Home">
            <select name="number_of_letters" id="number_of_letters" onChange={(e) => setNumberOfLetters(e.target.value)}>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
            </select>
            <form className="inputs-field" onSubmit={handleSubmit}>
                {rows}
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default Home
