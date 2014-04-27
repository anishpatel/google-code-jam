
object C extends App {
  val whitespace = raw"\s+".r
  val input = io.Source.stdin.getLines.flatMap(line => whitespace.split(line).map(_.toInt))
  val nCases = input.next
  for (c <- 1 to nCases) {
    val nRows = input.next()
    val nCols = input.next()
    val nCells = nRows * nCols
    val nMines = input.next()

    println(s"Case #$c:")
    if (nRows >= 2 && nCols >= 2) {
      if (nCells - nMines < 4)
        println("Impossible")
      else {
        // print possible board
      }
    } else {
      if (nCells - nMines >= 2)
        println("Impossible")
      else {
        // print possible board
      }
    }
  }
}
