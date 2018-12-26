def select_arr(arr)
  arr.select{|x| x%2!=0}
end

def reject_arr(arr)
  arr.delete_if{|x| x%3==0}
end

def delete_arr(arr)
    arr.delete_if{|x| x<=0}
end

def keep_arr(arr)
    arr.delete_if{|x| x>=0}
end
