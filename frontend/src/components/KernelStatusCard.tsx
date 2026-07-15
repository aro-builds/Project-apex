import { useKernel } from "../hooks/useKernel";

export default function KernelStatusCard() {

    const { agents, loading } = useKernel();

    if (loading) {

        return <p>Loading AI Kernel...</p>;

    }

    return (

        <div>

            <h2>AI Kernel</h2>

            <ul>

                {agents.map((agent: any) => (

                    <li key={agent.name}>

                        {agent.name} — {agent.status}

                    </li>

                ))}

            </ul>

        </div>

    );

}