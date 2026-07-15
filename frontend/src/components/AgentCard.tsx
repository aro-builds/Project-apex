interface Props {
    name: string;
    description: string;
    status: string;
}

export default function AgentCard({
    name,
    description,
    status,
}: Props) {

    return (

        <div className="bg-slate-800 rounded-xl p-4 shadow">

            <h2 className="text-xl font-bold">
                {name}
            </h2>

            <p className="text-gray-400">
                {description}
            </p>

            <span
                className={
                    status === "online"
                        ? "text-green-400"
                        : "text-red-400"
                }
            >
                {status}
            </span>

        </div>

    );

}