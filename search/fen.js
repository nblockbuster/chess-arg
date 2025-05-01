const colNames = ["a", "b", "c", "d", "e", "f", "g", "h"]

function isFen(maybeFen) {
    pattern = /^([0-9bknpqrBKNPQR]{1,8}\/){7}[0-9bknpqrBKNPQR]{1,8}$/gm

    return pattern.test(maybeFen);
}

function makeFen() {
    const cells = Array.from(document.querySelectorAll(".cell"))

    const fenList = []
    for (let i = 8; i > 0; i--) {
        const rowCells = cells.filter(el => el.id.includes(i.toString()));

        const row = colNames.map(
            c => {
                const cell = rowCells.find(el => el.id.includes(c));
                if (cell) {
                    return cell.getAttribute("data-piece") ?? 1
                }
                return 1;
            }
        );

        let rowString = ""
        let subtotal = 0
        for (let c of row) {
            if (typeof c == "number") {
                subtotal +=1;
            } else {
                if (subtotal !== 0) {
                    rowString += subtotal.toString();
                    subtotal = 0;
                }
                rowString += c;
            }
        }
        if (subtotal !== 0) {
            rowString += subtotal.toString();
        }

        fenList.push(rowString);
    }

    document.getElementById("fen").textContent = fenList.join("/")
}

function parseFen() {
    const fenInput = document.getElementById("fenInput");
    const fenError = document.getElementById("fenError");

    const fenString = fenInput.value;

    if (!isFen(fenString)) {
        fenError.textContent = `${fenString} is not a valid FEN`;
        fenInput.value = "";

        return;
    }

    resetBoard();
    fenError.textContent = "";

    fenString.split("/").forEach((fenLine, index) => {
        const rowIndex = 8-index;
        let colIndex = 0;
        for (const fenChar of fenLine) {
            if (isNaN(parseInt(fenChar))) {
                const id = `${colNames[colIndex]}${rowIndex}`;
                const cell = document.getElementById(id);

                if (cell) {
                    myglobals.piece = fenChar;
                    updateImage(cell);
                }
                colIndex += 1;
            } else {
                colIndex += parseInt(fenChar);
            }
        }
    });

    makeFen()
}