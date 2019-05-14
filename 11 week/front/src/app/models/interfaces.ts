interface TaskList{
    id: number,
    name: string
}

interface Task{
    id: number,
    name: string,
    created_at: Date,
    due_on: Date,
    status: string,
    task_list: TaskList
}

interface Post{
    id: number,
    title: string,
    body: string,
    like_count: number,
    created_at: Date,
    created_by: User
}

interface User{
    id: number,
    name: string
}