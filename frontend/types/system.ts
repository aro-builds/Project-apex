export interface SystemStatus {

    success: boolean;

    message: string;

    data: {

        system: string;

        version: string;

        services: {

            backend: string;

            ollama: string;

            workflow_engine: string;

            video_engine: string;

            voice_engine: string;

        };

    };

    timestamp: string;

}