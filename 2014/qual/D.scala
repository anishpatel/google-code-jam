
object D {
  def war(initNaoBlocks: Array[Double], initKenBlocks: Array[Double]) = {
    val naoBlocks = initNaoBlocks.reverseIterator
    val kenBlocks = initKenBlocks.toBuffer
    var points = 0

    for (naoBlock <- naoBlocks) {
      if (naoBlock > kenBlocks.last) {
        kenBlocks.trimStart(1)
        points += 1
      } else {
        kenBlocks.trimEnd(1)
      }
    }

    points
  }

  def deceitfulWar(initNaoBlocks: Array[Double], initKenBlocks: Array[Double]) = {
    val naoBlocks = initNaoBlocks
    val kenBlocks = initKenBlocks.toBuffer
    var points = 0

    for (naoBlock <- naoBlocks) {
      if (naoBlock < kenBlocks.head) {
        kenBlocks.trimEnd(1)
      } else {
        kenBlocks.trimStart(1)
        points += 1
      }
    }

    points
  }

  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines
    val nCases = input.next().toInt
    for (c <- 1 to nCases) {
      val nBlocks = input.next().toDouble
      val naoBlocks = input.next().split(' ').map(_.toDouble).sorted
      val kenBlocks = input.next().split(' ').map(_.toDouble).sorted

      val y = deceitfulWar(naoBlocks, kenBlocks)
      val z = war(naoBlocks, kenBlocks)

      println(f"Case #$c: $y $z")
    }
  }
}
