# Write your MySQL query statement below
select l.book_id,l.title,l.author,l.genre,l.publication_year,l.total_copies as current_borrowers
from library_books l join borrowing_records b
using (book_id)
where borrow_date is not null and return_date is null
group by book_id 
having count(book_id)=total_copies
order by current_borrowers desc,title


