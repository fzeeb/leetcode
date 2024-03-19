=begin
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.
=end
# @param {Character[]} tasks
# @param {Integer} n
# @return {Integer}
def least_interval(tasks, n)
    return tasks.length if n == 0
    task_count = tasks.each_with_object(Hash.new(0)) { |task, hash| hash[task] += 1 }
    max_count = task_count.values.max
    max_count_tasks = task_count.values.count(max_count)
    return [tasks.length, (max_count - 1) * (n + 1) + max_count_tasks].max
end

tasks = ["A","A","A","B","B","B"]
n = 2
puts least_interval(tasks, n) # 8