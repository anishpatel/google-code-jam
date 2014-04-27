import scala.collection.mutable.ArrayBuffer

object B extends App {
  val whitespace = raw"\s+".r
  val input = io.Source.stdin.getLines.flatMap(whitespace.split)
  val nCases = input.next().toInt
  for (c <- 1 to nCases) {
    val farmCost = input.next().toDouble
    val farmCookieRate = input.next().toDouble
    val nCookiesNeeded = input.next().toDouble

    var nFarms: Int = 0
    def totalCookieRate(nFarms: Int = nFarms) = 2.0 + nFarms * farmCookieRate
    def cookieMakeTime = nCookiesNeeded / totalCookieRate()

    val farmBuildTimeArr = ArrayBuffer(0.0)
    def farmBuildTime(nFarms: Int = nFarms): Double = {
      if (nFarms >= farmBuildTimeArr.length)
        farmBuildTimeArr.append(farmBuildTime(nFarms - 1) + farmCost / totalCookieRate(nFarms - 1))
      farmBuildTimeArr(nFarms)
    }
    def totalTime = farmBuildTime() + cookieMakeTime

    var lastBestTime = Double.MaxValue
    var currBestTime = totalTime
    while (currBestTime < lastBestTime) {
      lastBestTime = currBestTime
      nFarms += 1
      currBestTime = totalTime
    }

    println(f"Case #$c: $lastBestTime%.7f")
  }
}
