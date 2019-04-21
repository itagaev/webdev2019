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