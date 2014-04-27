
object A extends App {
  val whitespace = raw"\s+".r
  val input = io.Source.stdin.getLines.flatMap(line => whitespace.split(line).map(_.toInt))
  val nCases = input.next
  for (c <- 1 to nCases) {
    val row1 = input.next - 1
    val arrange1 = Array.fill(4, 4)(input.next)
    val row2 = input.next - 1
    val arrange2 = Array.fill(4, 4)(input.next)

    val intersection = arrange1(row1).toSet intersect arrange2(row2).toSet

    println(s"Case #$c: ${intersection.size match {
      case 1 => intersection.mkString
      case 0 => "Volunteer cheated!"
      case _ => "Bad magician!"
    }}")
  }
}
