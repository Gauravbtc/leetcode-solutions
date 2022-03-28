def merge(intervals)
 merged = []
  # sort intervals
  intervals.sort_by! { |interval| interval[0] }

  intervals.each do |interval|
    if merged.empty? || merged.last[1] < interval[0]
      merged << interval
    else
      merged.last[1] = interval[1] if interval[1] > merged.last[1]
    end
  end
  merged
end

# merge([[1,3],[2,6],[8,10],[15,18]])