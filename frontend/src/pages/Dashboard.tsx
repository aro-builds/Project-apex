import AgentCard from "../components/AgentCard";
import { useAgents } from "../hooks/useAgents";

export default function Dashboard() {

    const { agents, loading } = useAgents();

    if (loading) {
        return <h2>Loading...</h2>;
    }

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">
                Dashboard
            </h1>

            <div className="grid grid-cols-2 gap-4">

                {agents.map((agent: any) => (

                    <AgentCard
                        key={agent.name}
                        name={agent.name}
                        description={agent.description}
                        status={agent.status}
                    />

                ))}

            </div>

        </div>

    );

}