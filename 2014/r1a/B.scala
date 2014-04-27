import scala.collection.mutable

object B extends App {
  val whitespace = raw"\s+".r
  val input = io.Source.stdin.getLines().flatMap(whitespace.split)
  val T = input.next().toInt
  for (x <- 1 to T) {
    val N = input.next().toInt
    val edgesDense = Array.fill(N, N)(0)
    val edgesSparse = Array.fill(N)(mutable.Set[Int]())
    for (_ <- 0 until N - 1) {
      val n1 = input.next().toInt - 1
      val n2 = input.next().toInt - 1
      edgesDense(n1)(n2) = 1
      edgesSparse(n1) += n2
      edgesSparse(n2) += n1
    }
    var degreesArr = Array.fill(N)(0)
    var degreesMap = mutable.SortedMap[Int, List[Int]]().withDefaultValue(List[Int]())
    var degreesPQ =

    def compDegrees = {
      for (n <- 0 until N) {
        val rowSum = (0 until N) map (edgesDense(r)(n)) sum
        val colSum = (0 until N) map (edgesDense(n)(c)) sum
        degrees(n) = rowSum + colSum
        degreesMap(degrees(n)) = degrees(n) :: degreesMap(degrees(n))
      }
    }

    compDegrees
    while (degreesMap.max > 3)



    val y = if (minNFlips > L) "NOT POSSIBLE" else minNFlips
    println(s"Case #$x: $y")
  }
}
